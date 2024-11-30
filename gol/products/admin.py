from django.contrib import admin

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','purchase_price','selling_price', 'created_at')

admin.site.register(Product, ProductAdmin)