from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import RoommatePost, InterestedBuffer
from .serializers import RoommatePostGetSerializer, InterestedBufferGetSerializer
from rest_framework.response import Response


# Create your views here.

def greetThem(request):
    greeting = {'greeting' : "Hello, how are you?"}

    return JsonResponse(greeting)

def personalGreeting(request, name):
    greeting = {'greeting' : f"Hello {name}, how are you?"}

    return JsonResponse(greeting) # returns a JSON to the frontend, which can be very useful


# since the user should only have one roommate post, maybe add a boolean to their profile which signifies wheter they have a rommmate post or not, to update the frontend as needed

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUserRoommatePost(request):
    # from the user get the profile, then from the profile query for the 
    
    user_profile = request.user.profile # assigns the profile of the user to the variable 

    post = RoommatePost.objects.get(profile=user_profile) # will query for the nececsary post based on the given user profile (make sure that there can only be one roommate post per profile)

    serializer = RoommatePostGetSerializer(post, many=False) # will serialize into an appropriate form, which can then be converted into JSON to be sent back in the response

    return Response(serializer.data, status=status.HTTP_200_OK)


 # need to create a cursor pagination api to allow for the infinite scroll that we want to show on the frontend and have the frontend make the appropriate calls for the new data to have infinite feeling


 # function which will handle sending the interested roommates to frontend so it can be properly displayed 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def interestedRoommates(request):
    
    user_profile = request.user.profile # gets the profile of the user making the request to the variable 

    possibly_interested = InterestedBuffer.objects.get(owner=user_profile) # will get the buffer where the owner is this specific profile 

    serializer = InterestedBufferGetSerializer(possibly_interested, many=False) # there will only be one buffer which will need to get serialized

    return Response(serializer.data, status=status.HTTP_200_OK) # will return the serialized data in JSON format and put the proper status code 


# function which will handle adding the interested roommmate for furthur clarification