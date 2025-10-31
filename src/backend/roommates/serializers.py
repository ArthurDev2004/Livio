from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import RoommatePost
from features.serializers import FeatureSerializer
from profiles.serializers import ProfileGetSerializer

# serializer which will be used for GET requests for roommate posts (will be for the responses to get the GET requests)
class RoommatePostGetSerializer(ModelSerializer):

    # these serializers are for the nested serialization, so that instead of returning PK, it returns the actual objects, will be easier to handle on the front end
    features = FeatureSerializer(many=True) # this works with many being True, will also include the link to the icon images for each feature type
    #features = serializers.StringRelatedField(many=True) # this works, and only returns the names of the featurs which may be all that is needed
    profile = ProfileGetSerializer(many=False)



    class Meta:
        model = RoommatePost
        fields = ['title', 'description', 'originalPostDateTime', 'postLastUpdateDateTime', 'profile', 'features', 'funFact'] # these are the fields which will be serialized to JSON format and etc
    