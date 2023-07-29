from django import forms
from .models import*

class OrderForm(forms.ModelForm):
    class Meta():
        model = CartItem
        fields = ['drinkType', 'sizeType', 'sugarType', 'toppingType', 'quantity']

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = ['address', 'phoneNumber']