from django.apps import AppConfig


"""
Module Name: users.apps 
Date of Code: November 1, 2025
Programmer's Name: N/A
Description: Class is used by Django in configuring the apps section to work with the entire application. 
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
