from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group    


admin.site.site_header='Inventory admin Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity_in_stock')
    list_filter=('category',)

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)