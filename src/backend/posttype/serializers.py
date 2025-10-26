from rest_framework.serializers import ModelSerializer
from .models import PostType

class PostTypeSerializer(ModelSerializer):
    class Meta: 
        model = PostType
        fields = '__all__'