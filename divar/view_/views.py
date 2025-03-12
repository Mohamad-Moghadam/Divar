from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

product = {
    'name' : 'name',
    'price' : 'price',
    'sellers number' : 'number',
    'product photo' : 'the photo',
    'description' : 'description',
    'category' : 'category'
}

def show_product(request, product: str):
    product['category'] = product
    for i in range(100):
        return JsonResponse(product)