from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ApartmentPost, InterestedBuffer
from features.serializers import FeatureSerializer
from profiles.serializers import ProfileGetSerializer
from features.models import Feature

class ApartmentPostGetSerializer(ModelSerializer):
    
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