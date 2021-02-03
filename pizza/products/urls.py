from django.urls import path
from .views import *

urlpatterns = [
    path('products/',homepage,name='home'),
    path('about_us/',aboutus_page),
    path('contacts/',contact_page),
    path('registers/',register_page),
    path('users/',user_page),
    path('create_order/',create_order,name='create_order'),
    path('update_order/<int:order_id>/',update_order)
]