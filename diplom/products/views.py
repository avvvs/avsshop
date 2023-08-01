from datetime import datetime
from django.db.models import Q
from products.models import *
from django.shortcuts import render, get_object_or_404
from products.models import Product, Review
from products.forms import ReviewForm
from django.http import JsonResponse
import pytz


def home_page(request):  # Представление для домашней страницы
    products_images = ProductImage.objects.filter(is_active=True, main_image=True)
    products_images_phones_and_tablets = products_images.filter(product__product_type__id=2)
    products_images_laptops = products_images.filter(product__product_type__id=1)
    products_images_cameras = products_images.filter(product__product_type__id=3)
    return render(request, 'home.html', locals())


def product_page(request, product_id):  # Представление для страницы продукта
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user

            tz = pytz.timezone('Europe/Moscow')
            current_time = datetime.now(tz=tz)
            review.date_created = current_time

            review.save()

            data = {
                'status': 'success',
                'message': 'Review added successfully.',
            }
        else:
            data = {
                'status': 'error',
                'message': 'Invalid form data.',
            }
        return JsonResponse(data)

    form = ReviewForm()
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z%z'),
    }
    return render(request, 'product_page.html', context)


def search(request):  # Представление для поиска
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).prefetch_related(
            'productimage_set')
    else:
        results = []
    return render(request, 'search.html', {'results': results, 'query': query})


def chat(request):  # Представление для чата с умным ботом-консультантом
    products = Product.objects.all()
    product_names = [product.name for product in products]
    product_names = ', '.join(product_names)
    context = {
        'product_names': product_names,
    }
    return render(request, 'chat.html', context)


def laptops(request):  # Представление для страницы ноутбуков
    products_images = ProductImage.objects.filter(is_active=True, main_image=True)
    products_images_laptops = products_images.filter(product__product_type__id=1)
    return render(request, 'laptops.html', locals())


def phones_and_tablets(request):  # Представление для страницы телефонов и планшетов
    products_images = ProductImage.objects.filter(is_active=True, main_image=True)
    products_images_phones_and_tablets = products_images.filter(product__product_type__id=2)
    return render(request, 'phones_and_tablets.html', locals())


def cameras(request):  # Представление для страницы камер
    products_images = ProductImage.objects.filter(is_active=True, main_image=True)
    products_images_cameras = products_images.filter(product__product_type__id=3)
    return render(request, 'cameras.html', locals())


def hits(request):  # Представление для хитов продаж
    products_images = ProductImage.objects.filter(is_active=True, main_image=True)
    return render(request, 'hits.html', locals())


def about_us(request):  # Представление для страницы "О нас"
    return render(request, 'about_us.html')
