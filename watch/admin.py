from django.contrib import admin

# Register your models here.
from .models import Order,Product

class productAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Product,productAdmin)    
admin.site.register(Order)