from django.contrib import admin
from .models import Products

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ("name", "description", "price", "image", "active", "slug", "created_at", "updated_at")


admin.site.register(Products, AdminProduct)