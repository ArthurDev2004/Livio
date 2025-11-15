from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GenderSerializer
from .models import Gender

"""
Module: genders.views
Date: 2025-10-24
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Defines the API endpoint for creating Gender objects using Django REST
    Framework. This module is part of the Gender app and handles incoming
    POST requests that contain gender data formatted as JSON.

Design Pattern:
    - Decorator Pattern:
        The @api_view decorator wraps the function-based view and enforces
        allowed HTTP methods while enabling REST framework behavior.

    - Adapter Pattern:
        GenderSerializer adapts ORM model instances into JSON and vice versa.
"""

@api_view(['POST'])
def createGender(request):
    
    serializer = GenderSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)

    print(type(request.data))

    print(type(serializer.data))

    return Response(serializer.data, status=status.HTTP_201_CREATED)