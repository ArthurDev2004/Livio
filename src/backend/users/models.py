from django.db import models
import profiles.models 
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

"""
Module Name: users.models
Date of Code: October 30, 2025 - November 8, 2025
Programmer's Name: Arthur Lazaryan
Description:
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""

# custom user manager for the custom user class to create the user and to create a superuser as well 
class CustomUserManager(BaseUserManager):
   """
   Class Name: CustomerUserManager
   Date of Code: November 2, 2025
   Programmer's Name: Arthur Lazaryan
   Description: It is a custom implementation which overrides the create_user function of the regular User Manager class in Django. Allows for a custom User class to be implemented, instead of Django's prebuilt user class.
   Important Functions:
      create_user - used to create the user and save it with the neccesary fields 
         Input:
            username - the username of the user 
            email - the email of the user 
            password - the password of the user, which will get hashed in the function

         Output: 
            user - instance of the user which was just created
   """
   
   # this is the neccesary method for creating the custom user class (need to call this function to create the custom user)
   def create_user(self, username, email, password):
     """
     Function Name: create_user 
     Date of Code: November 2, 2025
     Programmer's Name: Arthur Lazaryan
     Description: Used to create the custom user class 
         Input:
            username - the username of the user 
            email - the email of the user 
            password - the password of the user, which will get hashed in the function

         Output: 
            user - instance of the user which was just created

     Data Structures: N/A
     Algorithms: N/A
     """
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
   """
   Class Name: User
   Date of Code: November 2, 2025
   Programmer's Name: Arthur Lazaryan
   Description: Represents the customer user object, which inherits the basics from the AbstractBaseUser so it can work with the manager above. 
   Important Functions: N/A
   Data Structures: 
      REQUIRED_FIELDS - Django specific which specifies which fields are required during creation of the object instance
      USERNAME_FIELD - Django specific which specifies which field is the unique identifying 'username' field for the user
   Algorithms: N/A
   """
   username: str = models.CharField(max_length=50, unique=True) # must be unique see it is being used as the username
   email: str = models.EmailField(max_length=50, unique=True)
   join_date = models.DateTimeField(null=False, auto_now_add=True) # this is the date in which the user joined, when new DB is made then use auto_now_add
   is_active = models.BooleanField(default=True) # this says that the user is an active user, and is used for auth

   REQUIRED_FIELDS = ['email'] # see if it works without this 
   USERNAME_FIELD = 'username'

   objects = CustomUserManager() # this is the custom user manager for creating new user, which will be called in the inital  

   # this will be the string representation for now 
   def __str__(self):
      """
      Function Name: __str__
      Description: Overloads the string function in python to provide string repersentation of the object 
      Input: None
      Output: str - username of the object, which is its string representation
      """
      return self.username
   
