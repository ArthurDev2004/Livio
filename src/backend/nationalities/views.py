from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Nationality
from .serializers import NationalitySerializer
from rest_framework import status

"""
Module: nationalities.views
Date: 2025-10-17
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    This module defines the API endpoints for retrieving and creating
    Nationality objects using Django REST Framework. It supports both
    single-object creation and bulk creation to help populate the database
    quickly during development.

Design Patterns:
    - Decorator Pattern:
        The @api_view decorator is applied to plain functions to add REST
        framework capabilities and enforce allowed HTTP methods.

    - Adapter Pattern:
        NationalitySerializer adapts ORM model instances into JSON and
        converts JSON data back to model instances for POST requests.
"""

# Create your views here.
@api_view(['GET'])
def allNationalities(request):
    nationalities = Nationality.objects.all() # returns all of the natioanlities which are saved in the db (in form of models of Django)

    print(type(nationalities[0])) # just to see the type of the nationality 

    serializer = NationalitySerializer(nationalities, many=True) # will serialize all of the nationalitiy models 

    return Response(serializer.data, status=status.HTTP_200_OK) # will return a list of json objects 


# will pass in many nationalities to it from postman, to create all of the nationalities quickly in the db 
@api_view(['POST'])
def createNationalities(request):
    
    # confirm that a list of nationality objects are being passed through the POST request 
    isList = isinstance(request.data, list) # will return a boolean 

    if isList == True: # handles case where there is a list of nationalities to be serialized
        serializer = NationalitySerializer(data=request.data, many=True) # will deserialize the JSON to models (confirm this)
    else:
        serializer = NationalitySerializer(data=request.data, many=False)

    if serializer.is_valid(): # performs validation checks defined in serializer (will need to update this)
        serializer.save() # saves the objects to the db 
        confirm = {'response' : 'confirmed'}

        return Response(confirm, status=status.HTTP_201_CREATED)
    else:

        return Response({'response' : 'went_wrong'}, status=status.HTTP_400_BAD_REQUEST)