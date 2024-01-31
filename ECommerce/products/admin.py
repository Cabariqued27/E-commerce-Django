from .models import Product
from django.contrib import admin


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')



admin.site.register(Product, ProductAdmin)