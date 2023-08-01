"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import diplom
import orders
import products.views
from products import views
from products.views import home_page
from orders.views import cart_adding
from django.conf import settings
from django.conf.urls.static import static
from .views import logout_view, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('product/<str:product_id>/', views.product_page, name='product'),
    path('cart_adding/', orders.views.cart_adding, name='cart_adding'),
    path('login/', diplom.views.login_view, name='login'),
    path('logout/', diplom.views.logout_view, name='logout'),
    path('register/', diplom.views.register_view, name='register'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('product/<int:product_id>/', views.product_page, name='product_page'),
    path('search/', views.search, name='search'),
    path('chat/', products.views.chat, name='chat'),
    path('order/', orders.views.order_page, name='order_page'),
    path('order_success/', orders.views.order_success_page, name='order_success'),
    path('laptops/', products.views.laptops, name='laptops'),
    path('phones_and_tablets/', products.views.phones_and_tablets, name='phones_and_tablets'),
    path('cameras/', products.views.cameras, name='cameras'),
    path('hits/', products.views.hits, name='hits'),
    path('about_us/', products.views.about_us, name='about_us'),

    # secretkey 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


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
