from django.db import models
from backend.profiles.models import Profile

# Create your models here.
class RoomatePost:
    # will need to add profile 
    profile: Profile = models.ForeignKey(to=Profile, on_delete=models.DO_NOTHING)
    # will need to add features here (will be a many to many relationship) 
    funFact: str = models.TextField()
    

