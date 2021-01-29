from django.shortcuts import render
from .models import Product,AboutUs

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    return render(request,'products/products.html',{"products":products})


def aboutus_page(request):
    about_us = AboutUs.objects.all()
    return render(request,'products/aboutsus.html',{"aboutsus":about_us})