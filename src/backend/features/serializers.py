from rest_framework import serializers
from .models import Feature

# will serialize the Feature obejct into the view
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'