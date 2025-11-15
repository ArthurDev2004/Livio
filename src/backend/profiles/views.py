from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileGetSerializer, ProfileCreationSerializer
from .models import Profile
from .conversions import convert, convert2

"""
Module Name: profiles.views 
Date of Code: October 17, 2025 - November 15, 2025
Programmer's Name: Arthur Lazaryan
Description: Has the function which will handdle whenever a certain endpoint is accessed. 
Important Functions:
    getProfile 

    getCurrentUserProfile

    createProfile

    editProfile 
Data Structures: N/A
Algorithms: N/A
"""

# test getting the profile 
@api_view(['GET'])
def getProfile(request):
    """
    Function Name: getProfile 
    Date of Code: October 17, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Gets all of the profiles available in the backend, serializes, and sends it to the frontend 

        Input:
           request - Django REST framework object which has all of the data that is sent in the request from the frontend to the backend

        Output:
            Response - Django REST framework implementation, which returns the profiles and the proper HTTP status code
    Data Structures: N/A
    Algorithms: N/A
    """

    profiles = Profile.objects.all() # gets a query set of all of the profiles

    serializer = ProfileGetSerializer(profiles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# get the profile of the current signed in user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserProfile(request):
    """
    Function Name: getCurrentUserProfile
    Date of Code: October 22, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Get the profile of the current user who is logged in 
    
        Input:
            request - Django REST framework object which has all of the data that is sent in the request from the frontend to the backend

        Output:
            Response - Django REST framework specific, which will return the current user's profile and the appropriate status code
    Data Structures: N/A
    Algorithms: N/A
    """

    profile = request.user.profile # using the related name, can access the profile of the current user based on the identification that comes from the JWT token

    serializer = ProfileGetSerializer(profile, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


# this will create a new profile 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProfile(request):
    """
    Function Name: createProfile 
    Date of Code: November 7, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will create the profile for the current user making the request, and will save it to the database 
        Input:
            request - Django REST framework object which has all of the data that is sent in the request from the frontend to the backend

        Output:
            Response - Django REST framework specific, which will return the current user's newly created profile and the appropriate status code
    Important Functions: N/A
    Data Structures: N/A
    Algorithms: N/A
    """
    
    # new_data = convert(request.data) # will return a new dictionary with the proper types that can be validated, and to work with is_valid() method

    # seems to have worked
    serializer = ProfileCreationSerializer(data=request.data, context={'request' : request.user}) # additional context is passed, which in this case is just the user which made the request, which is need to link the profile to the user, once created



    # the three other FK attributes are getting lost somehwere in the is_valid 
    if serializer.is_valid():
        # print(serializer.validated_data) # the validated data for some reason is not including the other three things, which have a FK relationship
        # works up until here --------------p
        serializer.save() # need to get this to work 

    # serializer = ProfileSerializer(data=request.data, context={'user': request.user}) # the context should pass in the user object, which will then be used to link the profile to the user in the one to one relationship

    # if serializer.is_valid(): # makes sure that the contents in which it is deserializing from JSON are valid to the proper model equivalents 
    #     print("This is what would have happened")
    #     serializer.save() # saves the data to the db (using the ORM), this choose wheter to call the create method or the update method 
    # else:
    #     print(serializer.errors)

    # use the get serializer to return the json

    # returnSerializer = ProfileGetSerializer(user_profile, many=False)

    return Response({"done" : "done"}, status=status.HTTP_201_CREATED) # returns the profile which was just created

# will be used to edit profile if the user chooses to do so
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editProfile(request):
    """
    Function Name: editProfile
    Date of Code: November 10, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will edit/update the profile with the new information passed in from the frontend. Uses the HTTP PUT method to indicate this is the case, just to follow best designs
        Input:
            request - Django REST framework object which has all of the data that is sent in the request from the frontend to the backend

        Output:
            Response - Django REST framework specific, which will return the current user's newly created profile and the appropriate status code
    Important Functions: N/A
    Data Structures: N/A
    Algorithms: N/A
    """
    
    # get the profile of the user making the request, and pass that instance into the serializer
    current_profile = request.user.profile 
    
    serializer = ProfileCreationSerializer(current_profile, data=request.data)

    if serializer.is_valid():
        print("Gets here")
        serializer.save() # will call the update method 

    print(serializer.errors)

    return Response({"done" : "done"}, status=status.HTTP_200_OK)
    