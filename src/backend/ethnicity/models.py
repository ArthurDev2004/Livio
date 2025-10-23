from django.db import models

# Create your models here.
class Ethnicity(models.Model):
    name: str = models.CharField(max_length=50)