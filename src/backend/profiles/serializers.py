from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Profile
from genders.models import Gender
from genders.serializers import GenderSerializer
from nationalities.models import Nationality
from nationalities.serializers import NationalitySerializer
from gradeLevels.models import GradeLevel
from gradeLevels.serializers import GradeLevelSerializer

# fix the create method for the serializer, see what is causing the issue of expected PK and etc 


# # will be used for serializing the json incoming to the django model which we need (first transforms to python objects, then those two models in django) (and vice versa)
# class ProfileSerializer(ModelSerializer):

#     # genderName = serializers.CharField(required=False) # putting the required argument to false makes it so that it is not needed 
#     # gradeLevelName = serializers.CharField(required=False)
#     # nationalityName = serializers.CharField(required=False)

#     # these will be the nested serializers 
#     gender =  serializers.SlugRelatedField(slug_field='name', read_only=True)
#     gradeLevel = serializers.SlugRelatedField(slug_field='name', read_only=True)
#     nationality = serializers.SlugRelatedField(slug_field='name', read_only=True)


#     # used to link the serializer to the class 
#     class Meta:
#         model = Profile
#         fields = '__all__' # all the fields will be included in the output of the serializer 

#     # validated_data is the POST JSON which was passed in
#     # can be used to have a custom logic for creating the POST data through the serializer and doing the neccesary things to create the profile in right way for the db 
#     def create(self, validated_data):

#         genderName = validated_data.pop('gender')
#         gradeLevelName = validated_data.pop('gradeLevel')
#         nationalityName = validated_data.pop('nationality')

#         # now find the actual objects from the db, so we can get the instances, and when we save it Django ORM will automatically handle the proper FK relationship
#         gender = Gender.objects.get(name=genderName)
#         gradeLevel = GradeLevel.objects.get(name=gradeLevelName)
#         nationality = Nationality.objects.get(name=nationalityName)

#         # have to get the user which will be linked with the profile
        

#         # this should now add the neccesary data objects, and the ORM can do the FK relationship for the DB 
#         profile = Profile.objects.create(gender=gender, gradeLevel=gradeLevel, nationality=nationality, profile_user=self.context['user'], **validated_data) # will pass in the rest of the data, and since it is a dictionary it will finish the keyword arguments 

#         return profile

#     # will need this whenever doing an update, can omit for now 
#     def update(self, validated_data):
#         pass

# will be used to deserialize the JSON and to create the neccesary model 
class ProfileCreationSerializer(ModelSerializer):

    # the slug related fields for the serializers take the string which was passed in, and make the deserialization take into accoutn the objects those strings are for and saves it like that 
    gender = serializers.SlugRelatedField(slug_field='name', queryset=Gender.objects.all()) # the query set is the set of models/objects which will be searched for a matching slug
    gradeLevel = serializers.SlugRelatedField(slug_field='name', queryset=GradeLevel.objects.all())
    nationality = serializers.SlugRelatedField(slug_field='name', queryset=Nationality.objects.all())

    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'gender', 'gradeLevel', 'nationality', 'bio'] # these are the fields that it should expect and work with when deserialzing the JSON



    # used to create the profile object 
    def create(self, validated_data):
        profile = Profile(**validated_data) # create teh profile with the validated data 
        profile.profile_user = self.context['request'] # adds the user to the profile 

        profile.save()

        return profile 
    
         

# this will be the serializer used in GET requests to return the actual name of the gender, nationality, and etc, instead of the primary keys of those attributes
class ProfileGetSerializer(ModelSerializer):
    gender = serializers.StringRelatedField(many=False) # will serialize the objects to their str function return values 
    gradeLevel = serializers.StringRelatedField(many=False)
    nationality = serializers.StringRelatedField(many=False)

    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'gender', 'gradeLevel', 'nationality', 'bio'] # these are the fields which the serializer/deserializer should worry about 