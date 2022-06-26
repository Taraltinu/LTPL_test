from django.contrib import admin
from ltpl_app.models import Product,Order,Brand,Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name","quantity"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_no","all_products"]