from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView


def login_view(request):  # Представление для авторизации
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):  # Представление для регистрации
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):  # Представление для выхода из аккаунта
    logout(request)
    return redirect('home_page')


class CustomPasswordResetView(PasswordResetView):  # Представление для смены пароля
    template_name = 'password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):  # Представление для смены пароля
    template_name = 'password_reset_done.html'
    success_url = reverse_lazy('login')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):  # Представление для смены пароля
    template_name = 'password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):  # Представление для смены пароля
    template_name = 'password_reset_complete.html'
    success_url = reverse_lazy('login')
