from django_registration.forms import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):  # Форма для входа
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                               strip=False,
                               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                 'placeholder': 'Password'}))


class CustomUserCreationForm(UserCreationForm):  # Форма для регистрации
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
