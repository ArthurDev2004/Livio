from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FeatureSerializer
from .models import Feature
from rest_framework import status

"""
Module: features.views
Date: 2025-11-7
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Provides API endpoints for retrieving feature objects used throughout the
    system. Features represent amenity tags or characteristics that can be
    attached to different post types (e.g., apartments, roommates).

Design Patterns:
    - Decorator Pattern:
        @api_view wraps function-based views and enforces allowed HTTP methods.

    - Adapter Pattern:
        FeatureSerializer adapts Django ORM Feature instances into JSON
        structures suitable for frontend consumption.
"""

# will get all of the features which we currently have
@api_view(['GET'])
def getFeatures(request):

    features = Feature.objects.all() # gets all of the features, they are models in djnago

    print(features[0].type)

    serializer = FeatureSerializer(features, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)




