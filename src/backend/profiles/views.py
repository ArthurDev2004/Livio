from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileGetSerializer, ProfileCreationSerializer
from .models import Profile
from .conversions import convert, convert2

# Create your views here.

# test getting the profile 
@api_view(['GET'])
def getProfile(request):

    profiles = Profile.objects.all() # gets a query set of all of the profiles

    serializer = ProfileGetSerializer(profiles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# get the profile of the current signed in user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserProfile(request):

    profile = request.user.profile # using the related name, can access the profile of the current user based on the identification that comes from the JWT token

    serializer = ProfileGetSerializer(profile, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


# this will create a new profile 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProfile(request):
    
    new_data = convert(request.data) # will return a new dictionary with the proper types that can be validated, and to work with is_valid() method

    # seems to have worked
    serializer = ProfileCreationSerializer(data=new_data, context={'request' : request.user}) # additional context is passed, which in this case is just the user which made the request, which is need to link the profile to the user, once created

    print(new_data['gradeLevel'])

    # the three other FK attributes are getting lost somehwere in the is_valid 
    if serializer.is_valid():
        # print(serializer.validated_data) # the validated data for some reason is not including the other three things, which have a FK relationship
        # works up until here --------------
        serializer.save() # need to get this to work 

    # serializer = ProfileSerializer(data=request.data, context={'user': request.user}) # the context should pass in the user object, which will then be used to link the profile to the user in the one to one relationship

    # if serializer.is_valid(): # makes sure that the contents in which it is deserializing from JSON are valid to the proper model equivalents 
    #     print("This is what would have happened")
    #     serializer.save() # saves the data to the db (using the ORM), this choose wheter to call the create method or the update method 
    # else:
    #     print(serializer.errors)

    # use the get serializer to return the json

    return Response(serializer.data, status=status.HTTP_201_CREATED) # returns the profile which was just created

