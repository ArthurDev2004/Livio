from django.db import models

"""
Module: nationalities.models
Date: 2025-10-17
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Defines the Nationality model used to store a user’s nationality in a
    normalized and consistent format. This model is used throughout the Profile
    system, roommate matching, and filtering functionality.

    Examples of possible nationality values:
        - "American"
        - "Indian"
        - "Mexican"
        - "Chinese"
        - "Sri Lankan"
        - etc.

Design Notes:
    - Normalizing nationality values prevents inconsistencies such as
      "usa", "USA", "American ", "american", etc.
    - Using a separate model allows future expansion (e.g., ISO country codes).
"""

class Nationality(models.Model):
    name: str = models.CharField(max_length=100)

    def __str__(self):
        return self.name