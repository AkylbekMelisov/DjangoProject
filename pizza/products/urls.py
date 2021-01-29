from django.urls import path
from .views import homepage,aboutus_page
# from .views import aboutus_page

urlpatterns = [
    path('products/',homepage),
    path('about_us/',aboutus_page)
]