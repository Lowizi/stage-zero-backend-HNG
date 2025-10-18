from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from decouple import config

class ProfileView(APIView):
    def get(self, request):
        try:
            cat_response = requests.get('https://catfact.ninja/fact', timeout=5)
            cat_response.raise_for_status()
            cat_fact = cat_response.json()['fact']
        except requests.RequestException:
            cat_fact = "Sorry, couldn't fetch a cat fact right now!"

        data = {
            "status": "success",
            "user": {
                "email": config('EMAIL'),
                "name": config('NAME'),
                "stack": config('STACK')
            },
            "timestamp": timezone.now().isoformat(),
            "fact": cat_fact
        }
        return Response(data, status=status.HTTP_200_OK, content_type='application/json')
