from django.utils.html import format_html
from django.contrib import admin
from sales.models import Product,Order,Brand,Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ["product_name","quantity","image_tag"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_no","all_products"]