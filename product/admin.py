from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'category', 'discount_price']
    prepopulated_fields = {'slug': ('title',)}
