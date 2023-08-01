from .models import CartOrder


def getting_cart_info(request):  # Контекстный процессор для получения информации о корзине
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key() if request.session.session_key else ''

    products_in_cart = CartOrder.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()

    return locals()
