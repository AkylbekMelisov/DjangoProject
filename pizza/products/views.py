from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
            return redirect('home')
    context = {"form":form}
    return render(request,'products/register.html',context)

def user_page(request):
    user = User.objects.all()
    context = {"users":user}
    return render(request,'products/users.html',context)

def create_order(request,product_id):
    product = Product.objects.get(id=product_id)
    total_price = 0
    form = OrderForm(initial={'product':product})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = product.price * form.cleaned_data['quantity']
            form.save()
    context = {"form":form,'total_price':total_price}
    return render(request,'products/create_order.html',context)

def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request,'products/create_order.html',context)


def delete_order(request,order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'order':order}
    return render(request,'products/delete.html',context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'products/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')
