from django.db import models
import profiles.models 
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# custom user manager for the custom user class to create the user and to create a superuser as well 
class CustomUserManager(BaseUserManager):
   
   # this is the neccesary method for creating the custom user class (need to call this function to create the custom user)
   def create_user(self, username, email, password):
     email = self.normalize_email(email) # will normalize email to the lowercase format 
     user = self.model(username=username, email=email)
     user.set_password(password) # should hash the password (figure out what is the hashing algorithm used)
     user.save()

     return user 

   # will need to provide a defintion whenever using the django admin 
   def create_superuser(self, username, email, password=None):
      pass
      

# custom user class 
class User(AbstractBaseUser): # will inherit stuff from the AbstractBaseUser but we can add our own fields as 
   username: str = models.CharField(max_length=50, unique=True) # must be unique see it is being used as the username
   email: str = models.EmailField(max_length=50, unique=True)
   join_date = models.DateTimeField(null=False, auto_now_add=True) # this is the date in which the user joined, when new DB is made then use auto_now_add
   is_active = models.BooleanField(default=True) # this says that the user is an active user, and is used for auth

   REQUIRED_FIELDS = ['email'] # see if it works without this 
   USERNAME_FIELD = 'username'

   objects = CustomUserManager() # this is the custom user manager for creating new user, which will be called in the inital  

   # this will be the string representation for now 
   def __str__(self):
      return self.username
   
