from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Имя"}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Фамилия"}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Email"}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Город"}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Адрес"}))
    postal_code = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Почтовый код"}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
