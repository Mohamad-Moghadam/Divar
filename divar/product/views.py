from django.shortcuts import render
from product.models import Product

def show_all_prducts(request):
    products = Product.objects.all()
    return render(request , 'product/product.html', {'products': products})
