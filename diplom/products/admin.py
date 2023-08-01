from django.contrib import admin
from products.models import Product, ProductImage, ProductType, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductTypeAdmin(admin.ModelAdmin):  # Тип продукта в административной панели
    list_display = [field.name for field in ProductType._meta.fields]

    class Meta:
        model = ProductType


admin.site.register(ProductType, ProductTypeAdmin)


class ProductAdmin(admin.ModelAdmin):  # Товары в административной панели
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):  # Картинки в административной панели
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class ReviewAdmin(admin.ModelAdmin):  # Отзывы в административной панели
    list_display = [field.name for field in Review._meta.fields]

    class Meta:
        model = Review


admin.site.register(Review, ReviewAdmin)
