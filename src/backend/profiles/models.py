from django.db import models
from genders.models import Gender
from gradeLevels.models import GradeLevel
from users.models import User
from nationalities.models import Nationality

# Create your models here.

# this is the model for the profile of the user 
class Profile(models.Model):
    firstName: str = models.CharField(max_length=20)
    lastName: str = models.CharField (max_length=50)
    age: int = models.IntegerField()
    gender: Gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, related_name='gender')
    gradeLevel: GradeLevel = models.ForeignKey(GradeLevel, on_delete=models.DO_NOTHING, related_name='gradeLevel') # these will be their own objects in the db, so that there is not much data repetition (sseems to be aggregation)
    nationality: Nationality = models.ForeignKey(Nationality, on_delete=models.DO_NOTHING, related_name='nationality')
    bio: str = models.TextField()
    profile_user: User = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=None, related_name='profile')
    #posts: list[Post] # will be a foriegn key relationship in post table 

    def __str__(self):
        return f"{self.firstName} {self.lastName}"