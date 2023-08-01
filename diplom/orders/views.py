from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from products.models import Product
from .models import CartOrder, Order


@login_required
def order_page(request):  # Представление для страницы заказа
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_cart = CartOrder.objects.filter(session_key=session_key, is_active=True)
    total_price = sum(item.total_price for item in products_in_cart)

    if request.method == 'POST':
        user = request.user if request.user.is_authenticated else None
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        order_comments = request.POST.get('order_comments')

        order = Order.objects.create(
            user=user,
            email=email,
            phone=phone,
            address=address,
            payment_method=payment_method,
            order_comments=order_comments,
            total_price=total_price
        )

        for item in products_in_cart:
            order.products.add(item.product, through_defaults={'quantity': item.nmb})

        # Очищаем корзину
        products_in_cart.delete()

        return redirect('order_success')

    return render(request, 'order.html', {'products_in_cart': products_in_cart, 'total_price': total_price})


def order_success_page(request):  # Представление для страницы успешного заказа
    return render(request, 'order_success.html')


def cart_adding(request):  # Представление для добавления в корзину
    return_dict = dict()

    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")

    is_delete = data.get("is_delete")
    if is_delete == 'true':
        CartOrder.objects.filter(id=product_id).update(is_active=False)
    else:
        product = get_object_or_404(Product, id=product_id)
        new_product_in_cart, created = CartOrder.objects.get_or_create(
            session_key=session_key,
            product=product,
            is_active=True,
            defaults={"nmb": nmb}
        )
        if not created:
            new_product_in_cart.nmb += int(nmb)
            new_product_in_cart.save(force_update=True)

    products_in_cart = CartOrder.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()

    return_dict["products_total_quantity"] = products_total_quantity

    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["reserve_price"] = item.reserve_price
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)
