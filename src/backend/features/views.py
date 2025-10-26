from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FeatureSerializer
from .models import Feature
from rest_framework import status


# will get all of the features which we currently have
@api_view(['GET'])
def getFeatures(request):

    features = Feature.objects.all() # gets all of the features, they are models in djnago

    print(features[0].type)

    serializer = FeatureSerializer(features, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)




