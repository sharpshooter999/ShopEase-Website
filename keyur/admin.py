
from django.contrib import admin
from keyur.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    filter_horizontal = ('recommended_products',)



