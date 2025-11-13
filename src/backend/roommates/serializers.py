from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import RoommatePost, InterestedBuffer
from features.serializers import FeatureSerializer
from profiles.serializers import ProfileGetSerializer, ProfilePaginationSerializer
from features.models import Feature

# serializer which will be used for GET requests for roommate posts (will be for the responses to get the GET requests)
class RoommatePostGetSerializer(ModelSerializer):

    # these serializers are for the nested serialization, so that instead of returning PK, it returns the actual objects, will be easier to handle on the front end
    features = FeatureSerializer(many=True) # this works with many being True, will also include the link to the icon images for each feature type
    #features = serializers.StringRelatedField(many=True) # this works, and only returns the names of the featurs which may be all that is needed
    profile = ProfileGetSerializer(many=False)



    class Meta:
        model = RoommatePost
        fields = ['title', 'description', 'originalPostDateTime', 'postLastUpdateDateTime', 'profile', 'features', 'funFact'] # these are the fields which will be serialized to JSON format and etc

# will be used to deserialize whenever getting data from a post request 
class RoommateCreationSerializer(ModelSerializer):

    # may be something wrong with this 
    features = serializers.SlugRelatedField(slug_field='name', queryset=Feature.objects.all(), many=True) # many signifies that it is used in a many to many relationship


    class Meta:
        model = RoommatePost
        fields = ['title', 'description', 'budget', 'funFact', 'moveInDate', 'features'] # these are the fields which should be handled in the deserialization, the dates will be handled by the DB 


    # override the create method to add the profile when the roommate post is being made
    def create(self, validated_data):
        post = RoommatePost()

        post.title = validated_data['title']
        post.description = validated_data['description']
        post.funFact = validated_data['funFact']
        post.budget = validated_data['budget']
        post.moveInDate = validated_data['moveInDate']
        post.profile = self.context['profile'] # puts the profile of the current user who made the request

        post.save() # need to save it first before can add the many to many relationship object

        post.features.set(validated_data['features']) # now can save the features (which have a many to many relationship), using the set method

        post.save()

        return post 
    
    # used whenever updating the roommate post
    def update(self, instance, validated_data):
        
        updateValues = list(validated_data.keys())

        for newField in updateValues:

            match(newField):
                case 'title':
                    instance.title = validated_data[newField]
                case 'description':
                    instance.description = validated_data[newField]
                case 'funFact':
                    instance.funFact = validated_data[newField]
                case 'budget':
                    instance.budget = validated_data[newField]   
                case 'moveInDate':
                    instance.moveInDate = validated_data[newField]
                case 'features':
                    instance.features.set(validated_data[newField])
                # no need to update the profile, since profile is the same, since same user

        instance.save()

        return instance

# this is the serializer which will be used for GET requests to get the interested buffer of that specific profile (will be for responses to get the GET requests)
class InterestedBufferGetSerializer(ModelSerializer):

    interestedProfiles = ProfileGetSerializer(many=True) # many is assigned true since there may be many profiles which are in the interested profiles

    class Meta:
        model = InterestedBuffer
        fields = ['bufferCount', 'interestedProfiles'] # only this field needs to get serialized during the GET request, because do not need to send information back like profile (owner) which will already be there 


# need to make it so that whenever a roommmate post is created for user, can have it also create the interested buffer for that user 
# can just pass in the id of the profile or something to get it going, instead of passing the entire profile 
class InterestedBufferAddSerializer(ModelSerializer):
    pass

# will be used in serializing for the pagination responses
class RoommatePaginationSerializer(ModelSerializer):
    
    features = FeatureSerializer(many=True) # will serialize the features 
    profile = ProfilePaginationSerializer(many=False) # will serialize to only get id of the profile of the current user

    class Meta:
        model = RoommatePost
        fields = ['title', 'description', 'funFact', 'budget', 'moveInDate', 'features', 'profile']
