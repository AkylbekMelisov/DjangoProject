from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homepage, name='home'),
    path('about_us/', aboutus_page, name='about_us'),
    path('contacts/', contact_page),
    path('registers/', register_page, name='register'),
    path('profiles/', profile_page, name='users'),
    path('create_order/<int:product_id>/', create_order, name='create_order'),
    path('update_order/<int:order_id>/', update_order),
    path('delete_order/<int:order_id>/', delete_order),
    path('sign_in/', sign_in, name='login'),
    path('logout/', logout_page, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='products/reset_password.html'),
         name='reset_password'),
    path('reset_password_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='products/reset_password_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='products/new_password.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         active_page, name='activate')
]
