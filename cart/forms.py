from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label='Количество', coerce=int, widget=forms.Select(attrs={'class': "select", }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
