from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
from .models import Order,Product

class productAdmin(admin.ModelAdmin):
    list_display = ["name"]
class orderAdmin(admin.ModelAdmin):
    fields = ["get_products_list","customer_name","number","comment"]
    list_display = ('customer_name','get_products',"products_list","number")
    def get_products(self,obj):
        return "\n".join([f"{product.name} ({product.newPrice})" for product in obj.products.all()])
        

    def products_list(self, obj):
        return "\n".join([f"{product.name} ({product.newPrice})" for product in obj.products.all()])

    def get_products_list(self, obj):
        a = [f'<tr><td style="font-weight:800;font-size:15px">{product.name}</td><td>{product.newPrice}</td></tr>' for product in obj.products.all()]
        list = "<table style='width:100%'><tr><th>name</th><th>price</th></tr>"
        for i in a:
            list = list+i
        list= list+"</table"
        #return format_html('<ul>{}</ul>'.join([f'<li><a href="">{product.name}</a> ({product.newPrice})</li>' for product in obj.products.all()]))
        return format_html(list)
    get_products_list.short_description = 'Products'
    readonly_fields = ('get_products_list',)    
    #get_products_list.short_description = 'Authors'

# class ProductInline(admin.TabularInline):
#     model = Product

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("customer_name","products")
# #     inlines = [ProductInline]
#     def products(self,obj):
#         return ", ".join([product.name for product in obj.products.all()])


admin.site.register(Product,productAdmin)    
admin.site.register(Order,orderAdmin)