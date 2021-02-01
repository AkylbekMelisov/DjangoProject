from django.urls import path
from .views import homepage,aboutus_page,contact_page,register_page

urlpatterns = [
    path('products/',homepage),
    path('about_us/',aboutus_page),
    path('contacts/',contact_page),
    path('registers/',register_page)
]