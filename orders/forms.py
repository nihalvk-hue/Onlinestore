from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    payment_screenshot = forms.FileField(required=False)
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'address', 'pincode', 'payment_screenshot', 'upi_transaction_id']
        