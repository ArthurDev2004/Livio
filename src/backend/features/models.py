from django.db import models
from posttype.models import PostType

"""
Module: features.models
Date: 2025-11-7
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam


Description:
    Defines the Feature model, which represents an attribute, amenity,
    or characteristic that can be attached to different types of posts
    such as ApartmentPost or RoommatePost.

    Each Feature is linked to a PostType object, allowing features to be
    categorized according to which type of post they apply to. This avoids
    hard-coding repeated feature names across different parts of the project.

Design Pattern:
    Bridge Pattern:
        This model uses a ForeignKey to the PostType model to bridge the
        "feature" concept with different post categories (e.g., Apartment,
        Roommate, Sublease). This allows flexibility and avoids deep inheritance
        trees or duplicate data.

Important Data Structures:
    - CharField: stores the feature name.
    - ForeignKey(PostType): links the feature to a specific post type.
    - URLField: stores the icon path for frontend display.
"""

# Create your models here.

# will be the feature class which will be used for many of the portions of the application
class Feature(models.Model):
    name: str = models.CharField(max_length=50)
    type: PostType = models.ForeignKey(PostType, on_delete=models.DO_NOTHING, default=0) # will keep it clean for each of the different type of posts, instead of having to repeat the same strings all the time 
    icon: str = models.URLField(null=True) # can make it null for the time being until we put an icon

    def __str__(self):
        return self.name
