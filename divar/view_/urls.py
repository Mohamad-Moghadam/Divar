from django.urls import path
from view_.views import show_product

urlpatterns = [
    path('<str:city>/<str:category>', show_product)
]