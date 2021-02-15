from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','description','price','size']


admin.site.register(Product,ProductAdmin)
admin.site.register([AboutUs,Order])
admin.site.register(Contacts)
admin.site.register(Document)
admin.site.register(Profile)
