from django.shortcuts import render
from .models import Product,AboutUs,Contacts
from .forms import register_forms

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    return render(request,'products/products.html',{"products":products})


def aboutus_page(request):
    about_us = AboutUs.objects.all()
    return render(request,'products/aboutsus.html',{"aboutsus":about_us})


def contact_page(request):
    contact = Contacts.objects.all()
    return render(request,'products/contacts.html',{"contacts":contact})


def register_page(request):
    form = register_forms
    context = {"form":form}
    return render(request,'products/register.html',context)
