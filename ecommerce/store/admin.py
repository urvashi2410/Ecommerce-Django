from django.contrib import admin
from .models import Product

# Register your models here.

# so that slug will be auto added as category name 
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

admin.site.register(Product, ProductAdmin)