from django.apps import AppConfig

"""
Module Name: posttype.apps 
Date of Code: October 15, 2025
Programmer's Name: N/A
Description: Class is used by Django in configuring the apps section to work with the entire application. 
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""


class PosttypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posttype'
