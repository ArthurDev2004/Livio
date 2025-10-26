from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GenderSerializer
from .models import Gender

# Create your views here.

@api_view(['POST'])
def createGender(request):
    
    serializer = GenderSerializer(data=request.data)
    
    serializer.is_valid()

    print(type(request.data))

    print(type(serializer.data))

    return Response(serializer.data, status=status.HTTP_201_CREATED)

