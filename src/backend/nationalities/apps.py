from django.apps import AppConfig

"""
Module: nationalities.apps
Date: 2025-10-17
Programmer: Arthur Lazaryan & Arrshan Saravanabavanandam

Description:
    Application configuration for the 'nationalities' app. This module registers
    the app within the Django project and can be extended in the future to
    include application-specific initialization logic such as signals or
    startup routines.

Design Notes:
    - Follows Django's AppConfig structure.
    - Uses 'BigAutoField' as the default primary key type for new models.
"""

class NationalitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nationalities'
