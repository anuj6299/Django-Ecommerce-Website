from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=250)

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=250)
    item_price = models.CharField(max_length=25)
    item_detail = models.CharField(max_length=2500)
    
