from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from decimal import Decimal


class ProductType(models.Model):  # Тип товара
    name = models.CharField(max_length=75, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Тип товаров'


class Product(models.Model):  # Товар
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True, default=None)
    specifications = models.TextField(blank=True, null=True, default=None)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField()
    discount = models.IntegerField(blank=True, null=True, default=0)
    product_type = models.ForeignKey(ProductType, blank=True, null=True, default=None, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # Переопределение метода save для учета скидки
        if self.discount:
            discount_amount = self.original_price * (Decimal(self.discount) / Decimal(100))
            self.price = self.original_price - discount_amount
            self.price = self.price.quantize(Decimal('.01'), rounding='ROUND_DOWN')
        else:
            self.price = self.original_price

        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):  # Карточка товара с картинкой
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images')
    is_active = models.BooleanField(default=True)
    main_image = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Review(models.Model):  # Отзыв
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
