from django.db import models
from posts.models import Post
from features.models import Feature
from profiles.models import Profile
from datetime import date
from genders.models import Gender
from nationalities.models import Nationality



class RoommatePost(Post):
    features: list[Feature] = models.ManyToManyField(Feature) # this tells the ORM that this is a many to many relationship and it will create the neccesary bridge entitiy table in the db
    funFact: str = models.TextField() # will be the fun fact  which will be used to display in the frontend
    budget: int = models.DecimalField(max_digits=10, decimal_places=2) # will be the budget they have for being a roommate 
    moveInDate = models.DateField(default=date.today) # this is the date that they can move in by; default is the current date

    def __str__(self):
        return f"{self.profile.firstName} {self.profile.lastName}'s Roommate Post"

    # look into the __ syntax for the queries

# need to create classes which are used to keep track of the profiles(people) they are interested in, and the ones which they are not
# can use the ones which they are not interested in, to filter out in further showings
# can use the ones which they are interested in on the side to see if they want to continue with messaging them

# has a FK to 
# class InterestedRoommate(models.Model):
#     profile = models.ForeignKey('profiles.profile', on_delete=models.DO_NOTHING)
#     interestedProfile = models.ForeignKey('profiles.profile', on_delete=models.DO_NOTHING)
#     pk = models.CompositePrimaryKey('profile', 'interestedProfile') # figure out way to have this be an appropriate primary key to not be duplicate since if the roles were resversed the primary key would be the same

# this is the buffer class which will hold the possible roommates this person is interested in, and will be there to allow them to message them 
class InterestedBuffer(models.Model): 
    # should probably specify that this FK is also the PK of the interested buffer (DO THIS)
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING) # the owner of the buffer 
    interestedProfiles: list[Profile] = models.ManyToManyField(Profile, db_table="Interested_Roommates", related_name="interested_profiles") # this tells ORM to make a bridge entity for the interested profiles for the many to many relationship
    bufferCount = models.IntegerField(default=0) # the size of the buffer, so do not need to always call a function to get the size 

    def __str__(self):
        return f"{self.owner.firstName} {self.owner.lastName}'s Interested Roommate Buffer"


# will serve as the bridge entity class between profile and interested buffer 
# class PossibleRoommates(models.Model):
#     interestedProfile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
#     buffer = models.ForeignKey(InterestedBuffer, on_delete=models.DO_NOTHING)
#     #bufferOwner = models.ForeignKey('profiles.Profile', on_delete=models.DO_NOTHING)

# class UninterestedRoommate(models.Model):
#     pass


# filter class which will have the logic for the filtering
class Filter:
    
    # filter on the budget specified on the post (NOT WORKING, FIGURE IT OUT)
    @staticmethod
    def budgetFilter(lowerBound: float, upperBound: float) -> list[RoommatePost]:
        posts = RoommatePost.objects.filter(budget__range=(lowerBound, upperBound)); # will query the db in the range 
        return posts # returns the queried roommate posts 
    
    # filter on the move in date specified on the post
    @staticmethod
    def moveInDateFilter(lowerBound: date, upperBound: date) -> list[RoommatePost]:
        posts = RoommatePost.objects.filter(moveInDate__range=(lowerBound, upperBound))
        return posts

    # filter on the gender of the profile who made the post 
    @staticmethod
    def genderFilter(gender: str) -> list[RoommatePost]:
        
        genderType = None 

        if gender == 'M':
            genderType = Gender.objects.get(name='M') # will get the gender object for male
        elif gender == 'F':
            genderType = Gender.objects.get(name='F') # will get the gender object for female
        else:
            genderType = Gender.objects.get(name='O') 

        posts = RoommatePost.objects.filter(profile__gender=genderType) # will filter based on that gender type (should be with the foreign key, see it works)

        return posts # should be a query set of objects (see if works when being serialized)
    

    # filter on the nationality of the profile who made the post 
    @staticmethod
    def nationalityFilter(nationality: str) -> list[RoommatePost]:

        nationalityType = Nationality.objects.get(name=str(nationality)) # get the nationality object 

        posts = RoommatePost.objects.filter(profile__nationality=nationalityType) # will filter based on the nationality of the person who made the post

        return posts 
        

    # filter based on the features which are present 
    @staticmethod
    def featuresFilter(features: list[dict[str, str]]) -> list[RoommatePost]:
        
        # do in backend for now, but there may be a better way to implement using Django and the DBMS 

        # go through each of the filter conditions, which are passed in from the frontend 
        for filterFeature in features:
            pass



    # can write the filter methods in a naive way now, and can refactor later

    # # this will be the main filter method that will be used
    # @staticmethod
    # def filter(criteria: str, value)