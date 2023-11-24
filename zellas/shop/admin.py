from django.contrib import admin
from .models import Category
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["title","description","get_thumbnail",]
    def get_thumbnail(self,obj):
        if obj.image:
            return format_html("<img src= {}  height='50px' />", obj.image.url)

