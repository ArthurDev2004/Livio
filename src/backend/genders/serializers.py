from rest_framework import serializers
from .models import Gender

# will deserialize the gender post request from JSON to a python/django model
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'