from django.db import models
from genders.models import Gender
from gradeLevels.models import GradeLevel
from posts.models import Post
from users.models import User

# Create your models here.
class Profile(models.Model):
    firstName: str = models.CharField(max_length=20)
    lastName: str = models.CharField (max_length=50)
    age: int = models.IntegerField()
    gender: Gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    gradeLevel: GradeLevel = models.ForeignKey(GradeLevel, on_delete=models.DO_NOTHING)
    bio: str = models.TextField()
    # may be non Django models 
    #user: User # may have to model as a one to one relationship
    #posts: list[Post]

