from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Profile
from genders.models import Gender
from genders.serializers import GenderSerializer
from nationalities.models import Nationality
from nationalities.serializers import NationalitySerializer
from gradeLevels.models import GradeLevel
from gradeLevels.serializers import GradeLevelSerializer

"""
Module Name: profiles.serializers
Date of Code: October 30, 2025 - November 10, 2025
Programmer's Name: Arthur Lazaryan
Description: Includes the different classes which are neccesary for serializing/deserializing the profile class
"""


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
    """
    Class Name: ProfileCreationSerializer 
    Date of Code: November 7, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will be used to deserialize the JSON data recieved from the frontend, and make neccesary queries in db to get the proper information together to save the new profile 
    Important Functions:
        create

        update 
    Data Structures: 
        SlugRelatedField - Django REST framework specific implementation for taking a slug (identifying string), can getting the matching object to it from the database
    Algorithms: N/A
    """

    # the slug related fields for the serializers take the string which was passed in, and make the deserialization take into accoutn the objects those strings are for and saves it like that 
    gender = serializers.SlugRelatedField(slug_field='name', queryset=Gender.objects.all()) # the query set is the set of models/objects which will be searched for a matching slug
    gradeLevel = serializers.SlugRelatedField(slug_field='name', queryset=GradeLevel.objects.all())
    nationality = serializers.SlugRelatedField(slug_field='name', queryset=Nationality.objects.all())

    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'gender', 'gradeLevel', 'nationality', 'bio', 'has_roommate_post'] # these are the fields that it should expect and work with when deserialzing the JSON



    # used to create the profile object 
    def create(self, validated_data):
        """
        Function Name: create 
        Date of Code: November 7, 2025
        Programmer's Name: Arthur Lazaryan
        Description: Used to create a profile class, and to do it in a custom way with a passed in context 
            Input:
                validated_data - the data which is passed in from the frontend to the backend in the format of a dictionary

            Output:
                profile - returns an instance of the newly created profile 
            
        Important Functions: N/A
        Data Structures:
            context - additional information which is passed in as a Python dictionary to add to the object when instantiating and saving it 
        Algorithms: N/A
        """
        profile = Profile(**validated_data) # create teh profile with the validated data 
        profile.profile_user = self.context['request'] # adds the user to the profile 

        profile.save()

        return profile 
    

    # will be used to update the profile object (needed for the update endpoint we have for the profile update)
    def update(self, instance, validated_data):
        """
        Function Name: update
        Date of Code: November 7, 2025
        Programmer's Name: Arthur Lazaryan
        Description: Used to update an instance of a profile class, when it is passed in to the serializer 
            Input:
                instance - instance of profile class which should be updated 

                validated_data - the data which is passed in from the frontend to the backend in the format of a dictionary

            Output:
                instance - returns the instance with the newly updated values 
        Important Functions: N/A
        Data Structures: N/A
        """
        
        updateValues = list(validated_data.keys()) # will create a list of the keys in the dictionary/JSON which was passed in

        print(updateValues)

        for field in updateValues:

            # will be used to match 
            match(field):
                case 'firstName':
                    instance.firstName = validated_data[field]
                case 'lastName':
                    instance.lastName = validated_data[field]
                case 'age':
                    instance.age = validated_data[field]
                case 'gender':
                    instance.gender = validated_data[field]
                case 'gradeLevel':
                    instance.gradeLevel = validated_data[field]
                case 'nationality':
                    instance.nationality = validated_data[field]
                case 'bio':
                    instance.bio = validated_data[field]
                case 'has_roommate_post':
                    instance.has_roommate_post = validated_data[field]

        
        instance.save() # saves it with the updated value 

        return instance 
    
         

# this will be the serializer used in GET requests to return the actual name of the gender, nationality, and etc, instead of the primary keys of those attributes
class ProfileGetSerializer(ModelSerializer):
    """
    Class Name: ProfileGetSerializer
    Date of Code: November 2, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will serialize the profile object in a way which is appropriate for the process of the frontend requesting it 
    Imporant Functions: N/A 
    Data Structures: 
        class Meta - specifies which model to serialize, and which fields in the model to serialize

        StringRElatedField - Will serialize the object to its string representation by their overiden str functions 
    Algorithms: N/A
    """
    gender = serializers.StringRelatedField(many=False) # will serialize the objects to their str function return values 
    gradeLevel = serializers.StringRelatedField(many=False)
    nationality = serializers.StringRelatedField(many=False)

    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'gender', 'gradeLevel', 'nationality', 'bio', 'has_roommate_post'] # these are the fields which the serializer/deserializer should worry about 


# will be used to only serialize the id from the Profile, which is all that will be needed for sending it back to the frontend in pagination
class ProfilePaginationSerializer(ModelSerializer):
    """
    Class Name: ProfilePaginationSerializer 
    Date of Code: November 2, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will serialize the profile to its id for the purposes of being used in pagination
    Important Functions: N/A
    Data Structures: 
        class Meta - specifies which model to serialize, and which fields in the model to serialize
    Algorithms: N/A
    """

    class Meta:
        model = Profile
        fields = ['id']