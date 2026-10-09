from django.db import models
from django.contrib import admin


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'quantity', 'description']

# Create your models here.
    