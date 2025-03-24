from django.shortcuts import render
from product.models import Product
import json
from django.shortcuts import get_object_or_404
from product.models import Product
from django.http import HttpResponse
from user.models import User
from django.views.decorators.csrf import csrf_exempt

def show_all_prducts(request):
    products = Product.objects.all()
    return render(request , 'product/product.html', {'products': products})

@csrf_exempt
def add_product(request, seller_id):
    if request.method == 'POST':
        seller = get_object_or_404(User, id=seller_id)

        data = json.loads(request.body)

        Product.objects.create(
            seller = seller,
            name = data.get('name'),
            location = data.get('location'),
        )

        return HttpResponse(f"{data.get('name')} was added as a new product.")
