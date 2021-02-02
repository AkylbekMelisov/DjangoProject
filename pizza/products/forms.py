from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


register_forms = UserCreationForm()

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product']