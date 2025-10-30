from django.db import models
import profiles.models 
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser): # will inherit stuff from the AbstractBaseUser but we can add our own fields as 
   username: str = models.CharField(max_length=50, unique=True) # must be unique see it is being used as the username
   email: str = models.EmailField(max_length=50, unique=True)
   join_date = models.DateTimeField(null=False, default=timezone.now) # this is the date in which the user joined, when new DB is made then use auto_now_add

   REQUIRED_FIELDS = ['email', ]
   USERNAME_FIELD = 'username'

   def __str__(self):
      return self.username