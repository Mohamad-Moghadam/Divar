from django.urls import path
from product.views import show_all_prducts

urlpatterns = [
    path('show-all', show_all_prducts)
]
