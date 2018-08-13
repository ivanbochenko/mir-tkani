from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Логин", 'autofocus': ""}))
    # first_name = forms.CharField(label='', max_length=30, required=False,
    #     widget=forms.TextInput(attrs={'name': 'Имя', 'class': "input is-large", 'placeholder': "Имя", 'autofocus': ""}))
    # last_name = forms.CharField(label='', max_length=30, required=False,
    #     widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Фамилия", 'autofocus': ""}))
    email = forms.EmailField(label='', max_length=254,
        widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Email", 'autofocus': ""}))
    password1 = forms.CharField(label='', widget=forms.TextInput(attrs={'type': "password", 'class': "input is-large", 'placeholder': "Пароль", 'autofocus': ""}))
    password2 = forms.CharField(label='', widget=forms.TextInput(attrs={'type': "password", 'class': "input is-large", 'placeholder': "Пароль ещё раз", 'autofocus': ""}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        # 'first_name', 'last_name', - removed


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Логин", 'autofocus': ""}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'type': "password", 'class': "input is-large", 'placeholder': "Пароль", 'autofocus': ""}))
