from django.db import models

# Create your models here.

# class/model for the general post class in application
class Post(models.Model):
    title: str = models.CharField(max_length=100); # post can have a title of max 100 characters in the db (VARCHAR(100))
    description: str = models.TextField(null=False) # description cannot be false in the database
    cost: float = models.DecimalField(max_digits=10, decimal_places=2)

    # the inner class is used by Django to get additional information
    class Meta:
        abstract = True # means that this class is an abstract base class, and it wont have its own table in the database (if done through Django ORM)