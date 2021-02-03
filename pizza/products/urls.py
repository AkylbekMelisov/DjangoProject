from django.urls import path
from .views import *

urlpatterns = [
    path('products/',homepage),
    path('about_us/',aboutus_page),
    path('contacts/',contact_page),
    path('registers/',register_page),
    path('users/',user_page),
    path('create_order/',create_order)
]