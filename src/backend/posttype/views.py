from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostTypeSerializer
from .models import PostType

"""
Module Name: posttype.views
Date of Code: October , 2025
Programmer's Name: Arthur Lazaryan
Description: Has the functions which will be used for creating and getting the posttypes available
Important Functions: N/A
Data Structures:
    @api_view  - Django REST framework decorator which is used for specifying the HTTP method that is used for the endpoint
Algorithms: N/A
"""


@api_view(['POST'])
def createPostType(request):
    """
    Function Name: createPostType
    Date of Code: October , 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will create post(s) from the data sent from the frontend

        Input:
            request - Django REST framework object which has all of the information passed in from the HTTP request 
        
        Output:
            Response - Django REST frameowrk specific with the newly created post type object data, and the appropriate HTTP status code

    Data Structures:
        PostTypeSerializer - used to deserialize the posttype object
    Algorithms: N/A
    """

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
    """
    Function Name: getPostTypes
    Date of Code: October , 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will return the posttypes objects to the frontend 

        Input:
            request - Django REST framework object which has all of the information passed in from the HTTP request 

        Output: 
            Response - Django REST framework specific for the posttype objects and the appropriate HTTP status code

    Data Structures: N/A

    Algorithms: 
        PostType.objects.all() - ORM usage to query the DB for the posttype objects
    """

    # get all of the post type objects from the db 
    postTypes = PostType.objects.all() 

    serializer = PostTypeSerializer(postTypes, many=True) # will serialize to the proper form, from complex model type to basic python types, to be sent back in the response 

    return Response(serializer.data, status=status.HTTP_200_OK) # the renderer in this response will do conversion to json




