from django.db import models
from posts.models import Post
from features.models import Feature



class RoommatePost(Post):
    features: list[Feature] = models.ManyToManyField(Feature) # this tells the ORM that this is a many to many relationship and it will create the neccesary bridge entitiy table in the db
    funFact: str = models.TextField() # will be the fun fact  which will be used to display in the frontend
    

# need to create classes which are used to keep track of the profiles(people) they are interested in, and the ones which they are not
# can use the ones which they are not interested in, to filter out in further showings
# can use the ones which they are interested in on the side to see if they want to continue with messaging them

# has a FK to 
class InterestedRoommate(models.Model):
    profile = models.ForeignKey('profiles.profile', on_delete=models.DO_NOTHING)
    interestedProfile = models.ForeignKey('profiles.profile', on_delete=models.DO_NOTHING)
    pk = models.CompositePrimaryKey('profile', 'interestedProfile') # figure out way to have this be an appropriate primary key to not be duplicate since if the roles were resversed the primary key would be the same


class UninterestedRoommate(models.Model):
    pass