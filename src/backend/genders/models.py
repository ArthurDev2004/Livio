from django.db import models

# Create your models here.
class Gender(models.Model):
    name: str = models.CharField(max_length=1)