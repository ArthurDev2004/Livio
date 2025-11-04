from django.db import models
from posts.models import Post
from features.models import Feature
from profiles.models import Profile



class RoommatePost(Post):
    features: list[Feature] = models.ManyToManyField(Feature) # this tells the ORM that this is a many to many relationship and it will create the neccesary bridge entitiy table in the db
    funFact: str = models.TextField() # will be the fun fact  which will be used to display in the frontend
    # add budget for the roommmate post; budget: int = models.IntegerField()
    # add move in ready to in; moveInDate = models.DateField() 
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

    # this will be the main filter method that will be used
    @staticmethod
    def filter(criteria: str, value):
        pass
    
    