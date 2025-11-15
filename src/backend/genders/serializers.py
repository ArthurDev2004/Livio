from rest_framework import serializers
from .models import Gender

"""
Module: genders.serializers
Date: 2025-10-24
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Provides the serializer used to convert Gender model instances to and from
    JSON format. This serializer allows frontend clients to send and receive
    gender information in a structured format.

Design Pattern:
    Adapter Pattern:
        Serializers adapt Django ORM model objects into simple JSON structures
        for the frontend, and convert JSON payloads back into Python model
        instances during POST/PUT operations.
"""

# will deserialize the gender post request from JSON to a python/django model
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'