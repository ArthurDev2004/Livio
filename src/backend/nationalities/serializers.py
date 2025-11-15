from rest_framework.serializers import ModelSerializer
from .models import Nationality

class NationalitySerializer(ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'