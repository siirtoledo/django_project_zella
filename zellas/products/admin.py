from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["title","description","get_thumbnail","category","price","created_at","updated_at"]
    list_display_links=["title"]
    def get_thumbnail(self,obj):
        if obj.image:
            return format_html("<img src= {}  height='50px' />", obj.image.url)


