from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FeatureSerializer
from .models import Feature
from rest_framework import status

# Create your views here.

def feature(request):
    return JsonResponse({'name' : 'Pet-Friendly'})

def postfeature(request):

    if request.method == 'POST':
        return JsonResponse({'name': 'Got the post!'})
    
    return JsonResponse({'name' : 'No get the post!'})

# view which is done with the rest framework way
@api_view(['GET'])
def createFeature(request):
    
    features = [Feature(name="Vegetarian", icon="blank"), Feature(name="Pet-Friendly", icon="blank"), Feature(name="No-Smoker", icon="blank")]

    serializer = FeatureSerializer(features, many=True) # will serialize the data into regular python data types from django models 

    return Response(serializer.data)


# as of now, it should just return the same content it received
@api_view(['POST'])
def new(request):

    serializer = FeatureSerializer(data=request.data)

    serializer.is_valid() # needs to be called prior to accessing its data attribute

    return Response(serializer.data, status=status.HTTP_201_CREATED) # added created status for the POST request



