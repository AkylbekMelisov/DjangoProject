from django.db import models

# Create your models here.
class Product(models.Model):
    categories = (
        ('vegan','vegan'),
        ('not_vegan','not_vegan'),
    )
    sizes = (
        ('small','small'),
        ('middle','middle'),
        ('great','great')
    )
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40,choices=categories)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    size = models.CharField(choices=sizes,max_length=50)


class AboutUs(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)


class Contacts(models.Model):
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    time = models.CharField(max_length=20)
    mng_name = models.CharField(max_length=40)
