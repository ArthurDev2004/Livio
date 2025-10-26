from django.db import models
from posts.models import Post
from features.models import Feature

# Create your models here.
class RoommatePost(Post):
    features: list[Feature] = models.ManyToManyField(Feature) # this tells the ORM that this is a many to many relationship and it will create the neccesary bridge entitiy table in the db
    funFact: str = models.TextField() # will be the fun fact  which will be used to display in the frontend
    

