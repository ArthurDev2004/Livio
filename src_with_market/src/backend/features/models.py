from django.db import models

# Create your models here.

# will be the feature class which will be used for many of the portions of the application
class Feature(models.Model):
    name: str = models.CharField(max_length=50) 
    icon: str = models.URLField(null=True) # can make it null for the time being until we put an icon
