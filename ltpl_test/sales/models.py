from django.db import models
from ltpl_accounts.models import User
from django.utils.html import escape
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=11,decimal_places=5)
    image = models.ImageField(upload_to ='product-img/%Y/%m/%d/')
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.product_name)



class Order(models.Model):
    order_no = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)
    total_qty = models.IntegerField()
    total_amount = models.DecimalField(max_digits=11,decimal_places=5)
    is_placed = models.BooleanField(default=False)
    product = models.ManyToManyField(Product) # generally we are handle it using orderitem table

    def all_products(self):
        return ",".join([str(p) for p in self.product.all()])

    def __str__(self):
        return str(self.order_no) 


