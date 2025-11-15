from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ApartmentPost, InterestedBuffer
from features.serializers import FeatureSerializer
from profiles.serializers import ProfileGetSerializer
from features.models import Feature

"""
Module: apartments.serializers
Date: 2025-11-14
Programmer: Arrshan Saravanabavanandam

Description:
    This module defines serializers for converting ApartmentPost model instances
    to and from JSON representations. These serializers serve as the translation
    layer between the backend Django models and the frontend API consumers.

    There are two serializers:
        - ApartmentPostGetSerializer: For retrieving apartment data (GET).
        - ApartmentPostCreateSerializer: For creating new listings (POST).

Design Patterns:
    - Adapter Pattern: Serializers act as adapters between Python model objects
      and JSON sent to/from the frontend.
    - Bridge Pattern: Feature relationship is handled through serializer linking.

Important Data Structures:
    - PrimaryKeyRelatedField: Used for feature_ids to map ManyToMany relations.
"""

class ApartmentPostGetSerializer(ModelSerializer):
    """
    Class: ApartmentPostGetSerializer
    Date: 2025-11-14
    Programmer: Arrshan Saravanabavanandam

    Description:
        Serializer used for retrieving ApartmentPost instances in a JSON format.
        Includes nested representations of profile and features for convenient
        frontend consumption.

    Inputs:
        ApartmentPost instance or queryset.

    Outputs:
        JSON-formatted dictionary including apartment details, amenities,
        timestamps, and associated profile information.
    """

    features = FeatureSerializer(many=True)
    profile = ProfileGetSerializer(many=False)
    
    class Meta:
        model = ApartmentPost
        fields = ['title', 
                  'description',
                      'address',
                      'city',
                      'state',
                      'zip_code',
                      'monthly_rent',
                      'bedrooms',
                      'bathrooms',
                      'square_feet',
                      'available_from',
                      'is_active', 
                      'originalPostDateTime', 
                      'postLastUpdateDateTime',]   
            
class ApartmentPostCreateSerializer(ModelSerializer):
    """
    Class: ApartmentPostCreateSerializer
    Date: 2025-11-14
    Programmer: Arrshan Saravanabavanandam

    Description:
        Serializer used for creating new apartment listings through POST requests.
        Accepts feature_ids instead of nested feature objects to simplify frontend
        data submission, mapping them to the ManyToManyField `features`.

    Inputs:
        JSON payload sent by frontend containing apartment information and feature IDs.

    Outputs:
        Validated ApartmentPost instance (not saved until .save() is called).
    """

    feature_ids = serializers.PrimaryKeyRelatedField(  
        many=True,
        queryset=Feature.objects.all(),
        source='features'  # Map to the 'features' field in the model
    )   
    
    class Meta:
        model = ApartmentPost
        fields = ['title', 
                  'description',
                  
                  'address',
                  'city',
                  'state',
                  'zip_code',
                  'monthly_rent',
                  'bedrooms',
                  'bathrooms',
                  'square_feet',
                  'available_from',
                  'is_active' ]