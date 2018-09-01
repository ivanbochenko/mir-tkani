from django import forms


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label='Количество', coerce=int, widget=forms.Select(attrs={'class': "select", }))
    quantity = forms.CharField(label='', widget=forms.TextInput(attrs={'style': "width: 80px;", 'type': "number", 'class': "input", 'placeholder': "Количество", 'step': "1", 'value': "10"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
