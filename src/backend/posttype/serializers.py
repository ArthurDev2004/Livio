from rest_framework.serializers import ModelSerializer
from .models import PostType

"""
Module Name: posttype.serializers 
Date of Code: October 15, 2025
Programmer's Name: Arthur Lazaryan
Description: Will be used to serialize the postype information to the frotnend if need be 
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""


class PostTypeSerializer(ModelSerializer):
    """
    Class Name: PostTypeSerializer
    Date of Code: October 15, 2025
    Programmer's Name: Arthur Lazaryan
    Description: Will be used to serialize the postype information to the frotnend if need be 
    Important Functions: N/A
    Data Structures:
        class Meta - specifies which model which the serializer is going to be used on
    Algorithms: N/A
    """

    class Meta: 
        model = PostType
        fields = '__all__'