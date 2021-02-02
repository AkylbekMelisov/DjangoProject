from django.contrib import admin
from .models import Product,AboutUs,Contacts,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','description','price','size']


admin.site.register(Product,ProductAdmin)
admin.site.register(AboutUs)
admin.site.register(Contacts)
admin.site.register(Order)