from django.db import models

"""
Module Name: posttype.models
Date of Code: October , 2025
Programmer's Name: Arthur Lazaryan
Description: Class which inherits from the Django Model class, will be used in our Features class just to specifiy the type of post that is being made so that appropriate "features" are used for the appropriate post type
Important Functions: N/A
Data Structures:
Algorithms:
"""


# Create your models here.
class PostType(models.Model):
    """
    Class Name: PostType
    Date of Code: October , 2025
    Programmer's Name: Arthur Lazaryan
    Description: Class which inherits from the Django Model class, will be used in our Features class just to specifiy the type of post that is being made so that appropriate "features" are used for the appropriate post type
    Important Functions: N/A
    Data Structures: N/A
    Algorithms: N/A
    """

    name: str = models.CharField(max_length=1) # will signify if housing post, roommate post, or marketplace post