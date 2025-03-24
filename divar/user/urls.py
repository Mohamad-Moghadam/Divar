from django.urls import path
from user.views import add_user


urlpatterns = [
    path('sign-up', add_user)
]
