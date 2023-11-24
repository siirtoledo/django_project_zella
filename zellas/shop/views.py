from django.shortcuts import render
from .models import Category
from products.models import Product

# Create your views here.
def home(request):
    category_data= Category.objects.all()
    product_data=Product.objects.all()
    return render(request, "index.html",{"category_data":category_data, "product_data":product_data})

    
    
