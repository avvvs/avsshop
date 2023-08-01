from django.contrib import admin
from orders.models import Order, OrderItem, OrderStatus, CartOrder


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderStatusAdmin(admin.ModelAdmin):  # Статус заказа в административной панели
    list_display = [field.name for field in OrderStatus._meta.fields]

    class Meta:
        model = OrderStatus


admin.site.register(OrderStatus, OrderStatusAdmin)


class OrderAdmin(admin.ModelAdmin):  # Заказ в административной панели
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderItemInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):  # Товар в заказе в административной панели
    list_display = [field.name for field in OrderItem._meta.fields]

    class Meta:
        model = OrderItem


admin.site.register(OrderItem, OrderItemAdmin)


class CartOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartOrder._meta.fields]

    class Meta:
        model = CartOrder


admin.site.register(CartOrder, CartOrderAdmin)
