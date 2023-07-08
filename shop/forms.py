from django import forms
from .models import*

class OrderForm(forms.ModelForm):
    class Meta():
        model = CartItem
        fields = ['drinkType', 'sizeType', 'sugarType', 'toppingType']