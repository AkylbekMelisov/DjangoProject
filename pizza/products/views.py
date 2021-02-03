from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Product,AboutUs,Contacts
from .forms import *


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
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request,'products/register.html',context)

def user_page(request):
    user = User.objects.all()
    context = {"users":user}
    return render(request,'products/users.html',context)

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request,'products/create_order.html',context)