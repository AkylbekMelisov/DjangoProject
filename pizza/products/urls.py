from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('about_us/',aboutus_page,name='about_us'),
    path('contacts/',contact_page),
    path('registers/',register_page,name='register'),
    path('users/',user_page,name='users'),
    path('create_order/<int:product_id>/',create_order,name='create_order'),
    path('update_order/<int:order_id>/',update_order),
    path('delete_order/<int:order_id>/',delete_order),
    path('sign_in/',sign_in,name='login')
]