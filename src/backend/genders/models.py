from django.db import models

# Create your models here.
class Gender(models.Model):
    name: str = models.CharField(max_length=1)

    def __str__(self):

        if self.name == 'M':
            return 'Male'
        else:
            return 'Female'
        