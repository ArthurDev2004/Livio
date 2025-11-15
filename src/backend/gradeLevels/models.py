from django.db import models

# Create your models here.
class GradeLevel(models.Model):
    name: str = models.CharField(max_length=8)

    def __str__(self):
        return self.name