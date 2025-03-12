from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

products = {
    'name' : 'name',
    'price' : 'price',
    'sellers number' : 'number',
    'product photo' : 'the photo',
    'description' : 'description',
    'category' : 'category'
}

def show_products(request, category):
    products['category'] = category
    for i in range(100):
        return JsonResponse(products)
