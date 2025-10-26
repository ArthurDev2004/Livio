from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostTypeSerializer
from .models import PostType

# Create your views here.

@api_view(['POST'])
def createPostType(request):

    # check if the request is a list of json or an individual json
    isList = isinstance(request.data, list)

    if isList == True:
        serializer = PostTypeSerializer(data=request.data, many=True)
    else:
        serializer = PostTypeSerializer(data=request.data, many=True)

    if serializer.is_valid():
        serializer.save() # saves the post types
        return Response({'response' : 'confirmed'}, status=status.HTTP_201_CREATED)

# will return all of the 
@api_view(['GET'])
def getPostTypes(request):

    # get all of the post type objects from the db 
    postTypes = PostType.objects.all() 

    serializer = PostTypeSerializer(postTypes, many=True) # will serialize to the proper form, from complex model type to basic python types, to be sent back in the response 

    return Response(serializer.data, status=status.HTTP_200_OK) # the renderer in this response will do conversion to json




