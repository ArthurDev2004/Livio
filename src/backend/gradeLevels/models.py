from django.db import models

"""
Module: gradeLevels.models
Date: 2025-10-24
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Defines the GradeLevel model, which represents a user’s academic standing
    or school year in a normalized format (e.g., 'Freshman', 'Junior',
    'Senior', 'Graduate'). This model is primarily used within the Profile app
    and for roommate-matching filters.

Design Notes:
    - This model normalizes academic levels instead of storing free text.
    - Makes filtering and grouping by grade level more consistent.
"""

# Create your models here.
class GradeLevel(models.Model):
    name: str = models.CharField(max_length=8)

    def __str__(self):
        return self.name