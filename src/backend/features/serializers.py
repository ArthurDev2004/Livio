from rest_framework import serializers
from .models import Feature

# will serialize the Feature obejct into the view
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name', 'icon'] # do not need posttype to serialize since that is only needed for the backend
        # depth = 1 # makes it so that the foreign key (which is nested at one level in) will be able to be returned the actual object, not just the foreign key