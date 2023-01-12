from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'product_name', 'price', 'stock', 'category', 'created_at', 'is_active', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ('is_active','is_available', 'category')
    search_fields = ('product_name',)
    ordering = ('product_name',)
    readonly_fields = ('image_tag',)
    list_per_page = 10

# Register your models here.
admin.site.register(Product, ProductAdmin)