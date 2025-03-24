from django.shortcuts import render
from product.models import Product
import json
from product.models import Product

def show_all_prducts(request):
    products = Product.objects.all()
    return render(request , 'product/product.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Product.objects.create(
            seller_id = data.get('seller'),
            name = data.get('name'),
            location = data.get('location'),
        )
