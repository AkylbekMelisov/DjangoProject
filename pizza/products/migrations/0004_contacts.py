# Generated by Django 3.1.5 on 2021-01-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
                ('time', models.CharField(max_length=20)),
                ('mng_name', models.CharField(max_length=40)),
            ],
        ),
    ]