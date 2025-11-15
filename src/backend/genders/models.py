from django.db import models

"""
Module: genders.models
Date: 2025-10-24
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Defines the Gender model used for storing a user's gender in a normalized,
    consistent format. The system uses a single-character code ('M' or 'F')
    and maps it to a human-readable form for display.

Design Notes:
    - This model normalizes gender values to prevent inconsistent free-text
      entries such as “male”, “Male ”, “M”, etc.
    - The __str__ method returns a readable value, which is useful in admin pages
      and serializer displays.

Important Data Structures:
    - CharField(max_length=1): Stores a single-letter gender code.
"""

# Create your models here.
class Gender(models.Model):
    name: str = models.CharField(max_length=1)

    def __str__(self):

        if self.name == 'M':
            return 'Male'
        else:
            return 'Female'
        