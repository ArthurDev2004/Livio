from django.db import models
import profiles.models 

# Create your models here.
class User(models.Model):
    email: str = models.CharField(max_length=100)
    usename: str = models.CharField(max_length=100)
    # password 
    # profile: profiles.models.Profile = models.ForeignKey(profiles.models.Profile, on_delete=models.DO_NOTHING)