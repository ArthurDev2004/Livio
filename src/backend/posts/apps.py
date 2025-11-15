from django.apps import AppConfig

"""
Module Name: posts.apps 
Date of Code: October 15, 2025
Programmer's Name: N/A
Description: Class is used by Django in configuring the apps section to work with the entire application. 
Important Functions: N/A
Data Structures: N/A
Algorithms: N/A
"""


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
