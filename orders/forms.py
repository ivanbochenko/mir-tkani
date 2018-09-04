from django import forms
from .models import Order


CHOICES = [('Наличными', 'Наличными'), ('Карта Приват Банка', 'Карта Приват Банка')]


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "ФИО"}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Телефон"}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Email"}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Город"}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Адрес"}))
    postal_code = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Почтовый код"}))
    post_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "input is-large", 'placeholder': "Номер склада"}))
    payment = forms.ChoiceField(label='Оплата', choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Order
        fields = ['first_name', 'phone', 'email', 'city', 'address', 'postal_code', 'post_number', 'payment']
