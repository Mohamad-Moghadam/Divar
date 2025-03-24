from django.shortcuts import render
import json
from user.models import User

def add_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        User.objects.create(
            name = data.get("name"),
            number = data.get("number"),
            national_id_number = data.get("national_id_number"),
        )
