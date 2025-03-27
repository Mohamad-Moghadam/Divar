from django.urls import path
from product.views import show_all_prducts, add_product

urlpatterns = [
    path('show-all', show_all_prducts),
    path('add-product/<int:seller_id>', add_product)
]
