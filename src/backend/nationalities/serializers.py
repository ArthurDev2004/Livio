from rest_framework.serializers import ModelSerializer
from .models import Nationality

"""
Module: nationalities.serializers
Date: 2025-10-17
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Provides the serializer used to convert Nationality model instances to and
    from JSON format. This serializer is used when sending nationality data to
    the frontend (e.g., displaying a dropdown of nationalities) and when
    receiving nationality information from POST/PUT requests.

Design Pattern:
    Adapter Pattern:
        Serializers serve as an adapter that transforms Django ORM model
        instances into JSON structures usable by the frontend, and also validate
        and convert incoming JSON back into Python model instances during
        data creation or updates.
"""

class NationalitySerializer(ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'