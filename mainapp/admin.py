from django.contrib import admin
from mainapp.models import ProductCategory, Product
# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'quantity',)
    # readonly_fields = ('name',)
    # list_editable = ('name', 'price','quantity',)
