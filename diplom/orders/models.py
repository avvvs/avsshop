from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class OrderStatus(models.Model):  # Статус заказа
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Статус заказа #{self.name}"

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):  # Заказ
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_comments = models.TextField(max_length=255, blank=True, null=True, default=None)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default='1')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return f"Заказ #{self.pk} x {self.order_status.name}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):  # Товар в заказе
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, default=None)
    quantity = models.IntegerField(default=1)
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    is_active = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} x {self.quantity} в заказе #{self.order.pk}"

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.reserve_price = self.product.price
        total_price = self.quantity * self.reserve_price
        self.total_price = total_price
        order = self.order
        all_products_in_order = OrderItem.objects.filter(order=order, is_active=True)
        order_total_price = 0
        for item in all_products_in_order:
            order_total_price += item.total_price
        order.total_price = order_total_price + total_price
        order.save(update_fields=['total_price'])
        super(OrderItem, self).save(*args, **kwargs)


class CartOrder(models.Model):  # Товар в корзине
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, default=None, null=True)
    nmb = models.IntegerField(default=1)
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    is_active = models.BooleanField(default=True)
    session_key = models.CharField(max_length=256, default=None, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        if self.product:
            self.reserve_price = self.product.price if self.product else 0
            self.total_price = int(self.nmb) * self.reserve_price

        super(CartOrder, self).save(*args, **kwargs)

