from rest_framework import serializers
from .models import Feature

"""
Module: features.serializers
Date: 2025-11-7
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Provides serializer classes for converting Feature model instances into
    JSON format for API responses. Serializers act as the translation layer
    between Django model objects and frontend-ready JSON data.

Design Pattern:
    Adapter Pattern:
        Serializers adapt complex Django ORM objects into simple JSON structures
        that can be consumed by the frontend. This allows frontend clients to
        remain decoupled from backend model implementation details.

Important Notes:
    - Only the 'name' and 'icon' fields are exposed because the PostType
      relationship is only required internally for backend organization.
"""

# will serialize the Feature obejct into the view
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name', 'icon'] # do not need posttype to serialize since that is only needed for the backend
        # depth = 1 # makes it so that the foreign key (which is nested at one level in) will be able to be returned the actual object, not just the foreign key