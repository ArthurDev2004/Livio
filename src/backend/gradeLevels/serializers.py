from rest_framework.serializers import ModelSerializer
from .models import GradeLevel

class GradeLevelSerializer(ModelSerializer):
    class Meta:
        model = GradeLevel
        fields = '__all__'

        