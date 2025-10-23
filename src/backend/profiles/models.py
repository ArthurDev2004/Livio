from django.db import models
from backend.ethnicity.models import Ethnicity
from backend.genders.models import Gender
from backend.gradeLevels.models import GradeLevel
from backend.posts.models import Post
from backend.users.models import User

# Create your models here.
class Profile(models.Model):
    firstName: str = models.CharField(max_length=20)
    lastName: str = models.CharField (max_length=50)
    age: int = models.IntegerField()
    gender: Gender = models.ForeignKey(to=Gender, on_delete=models.DO_NOTHING)
    gradeLevel: GradeLevel = models.ForeignKey(to=GradeLevel, on_delete=models.DO_NOTHING)
    ethnicity: Ethnicity = models.ForeignKey(to=Ethnicity, on_delete=models.DO_NOTHING) # it is do nothing for now, but need to go back and change it
    bio: str = models.TextField()
    # may be non Django models 
    user: User 
    posts: list[Post]

