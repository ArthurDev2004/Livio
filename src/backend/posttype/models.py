from django.db import models

# Create your models here.
class PostType(models.Model):
    name: str = models.CharField(max_length=1) # will signify if housing post, roommate post, or marketplace post