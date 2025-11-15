from rest_framework.serializers import ModelSerializer
from .models import GradeLevel

"""
Module: gradeLevels.serializers
Date: 2025-10-24
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Provides the serializer used to convert GradeLevel model instances to and
    from JSON format. This serializer enables the frontend to retrieve all
    academic grade level values and allows the backend to process POST/PUT
    requests that include grade level data.

Design Pattern:
    Adapter Pattern:
        Serializers act as adapters that convert complex Django ORM objects into
        simple JSON structures for the frontend, and convert JSON payloads back
        into Python objects during create/update operations.
"""

class GradeLevelSerializer(ModelSerializer):
    class Meta:
        model = GradeLevel
        fields = '__all__'