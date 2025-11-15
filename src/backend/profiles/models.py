from django.db import models
from genders.models import Gender
from gradeLevels.models import GradeLevel
from users.models import User
from nationalities.models import Nationality

"""
Module Name: profiles.models
Date of Code: October 17, 2025
Programmer's Name: Arthur Lazaryan
Description: It is the profile class for the user of the application. Has more detailed profile information on the user
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""

# this is the model for the profile of the user 
class Profile(models.Model):
    """
    Class Name: Profile 
    Date of Code: October 17, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Is the profile class for the user of the application, and includes more detailed profile information on the user
    Important Functions: 
        __str__ - provides string representation of the object 

    Data Structures:
        Specific Django implementations are provided to match the neccesary constraints of the fields, so it works with the ORM in the relational model 
    
    Algorithms: N/A
    """
    firstName: str = models.CharField(max_length=20)
    lastName: str = models.CharField (max_length=50)
    age: int = models.IntegerField()
    gender: Gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, related_name='gender')
    gradeLevel: GradeLevel = models.ForeignKey(GradeLevel, on_delete=models.DO_NOTHING, related_name='gradeLevel') # these will be their own objects in the db, so that there is not much data repetition (sseems to be aggregation)
    nationality: Nationality = models.ForeignKey(Nationality, on_delete=models.DO_NOTHING, related_name='nationality')
    bio: str = models.TextField()
    profile_user: User = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=None, related_name='profile')
    has_roommate_post: bool = models.BooleanField(default=False) # will indicate wheter the profile has a roommate post or not, and if so, will be used to know which page to show them
    #posts: list[Post] # will be a foriegn key relationship in post table 

    def __str__(self):
        """
        Function Name: __str__
        Description: Provides string representation of the profile object, which is just the frist and last name
        Input: None
        Output: str - first and last name
        """
        return f"{self.firstName} {self.lastName}"