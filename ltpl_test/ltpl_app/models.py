from email.mime import image
from itertools import product
from operator import mod
from django.db import models
from ltpl_accounts.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=11,decimal_places=5)
    image = models.ImageField(upload_to ='product-img/%Y/%m/%d/')
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

class Order(models.Model):
    order_no = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quentity = models.IntegerField()
    ordered_on = models.DateTimeField(auto_now_add=True)
    total_qty = models.IntegerField()
    total_amount = models.DecimalField(max_digits=11,decimal_places=5)
    is_placed = models.BooleanField(default=False)
    product = models.ManyToManyField(Product) # generally we are handle it using orderitem table

    def all_products(self):
        return ",".join([str(p) for p in self.product.all()]) 


