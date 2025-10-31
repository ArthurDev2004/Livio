from django.db import models
from posttype.models import PostType

# Create your models here.

# will be the feature class which will be used for many of the portions of the application
class Feature(models.Model):
    name: str = models.CharField(max_length=50)
    type: PostType = models.ForeignKey(PostType, on_delete=models.DO_NOTHING, default=0) # will keep it clean for each of the different type of posts, instead of having to repeat the same strings all the time 
    icon: str = models.URLField(null=True) # can make it null for the time being until we put an icon

    def __str__(self):
        return self.name
