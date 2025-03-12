from django.urls import path
from search.views import show_products

urlpatterns = [
    path('<str:city>/<str:category>', show_products)
]
