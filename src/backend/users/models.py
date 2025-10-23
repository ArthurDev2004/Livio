from django.db import models
from backend.profiles.models import Profile

# Create your models here.
class User(models.Model):
    email: str = models.CharField(max_length=100)
    usename: str = models.CharField(max_length=100)
    # password 
    profile: Profile = models.ForeignKey(to=Profile, on_delete=models.DO_NOTHING)