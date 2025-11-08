from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import RoommatePost, InterestedBuffer
from .serializers import RoommatePostGetSerializer, InterestedBufferGetSerializer, RoommateCreationSerializer
from rest_framework.response import Response
from profiles.models import Profile


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


# create the roommate post (Figure out why it is not working)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRoommatePost(request):
    # will get the profile from the user which is passed from the JWT auth
    # will need to receive funfact 
    # will need to receive the budget 
    # will need to receive the moveInDate 
    # will need to receive a list of features 
    # will need to get title for the post
    # will need to get description of the post 
    # maybe need to set the value of wheter the profile has a roommate post to true, to indicate that it has a roommate post, and to not allow for more to be called

    # when creating a roommate post, need to make it so that a interested buffer is created at the same time

    # need to add a restriction that once the the user has a roommate post it cannot add this any longer

    # will create the interested buffer for the current user who is making a new roommate post, since now that they have a roommate post, it is possible for them to add a interested profiles
    new_interested_profile_buffer = InterestedBuffer(bufferCount=0, owner=request.user.profile) # the buffer has a FK relationship with profile and a many to many relationship (FK designates owner, and )
    new_interested_profile_buffer.save() # will save the buffer in the db so it can be used whenver the user needds it

    serializer = RoommateCreationSerializer(data=request.data, context={"profile" : request.user.profile}) # deserializes from JSON to a type suitable (Django Model) to be used and saved to the db

    if serializer.is_valid():
        serializer.save() 

    print(serializer.errors)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

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
# will be a POST request 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addInterestedRoommate(request):
    # will pass the profile id of the roommate they are interested in
    # then this will add that profile to the list of profiles they are interested in
    # will send some info to the frontend, when querying the list
    
    current_user_profile = request.user.profile 
    current_user_interested_buffer = InterestedBuffer.objects.get(owner=current_user_profile) # gets the buffer which holds the profiles which the current user is interested in

    # gets the profile which the user is interested in to be roommates
    interested_profile_id = request.data['id'] # will be the id of the profile which this current user is interested in
    interested_profile = Profile.objects.get(pk=interested_profile_id) # will get the profile with that id 
    # will add that profile to this current person's interested buffer, and save that 

    # seems to be something wrong here, with the step below
    current_user_interested_buffer.interestedProfiles.add(interested_profile) # adds the interested profile to the current profile's interested buffer
    current_user_interested_buffer.bufferCount = current_user_interested_buffer.bufferCount + 1; # add one to buffer count for the new profile which was added to the buffer
    current_user_interested_buffer.save() # saves it to the db with the proper bridge entity and etc

    serializer = InterestedBufferGetSerializer(current_user_interested_buffer, many=False) # will serialize to 

    return Response(serializer.data, status=status.HTTP_201_CREATED)


    