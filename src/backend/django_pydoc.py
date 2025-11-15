import django 
import pydoc
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livio_project.settings')

django.setup() # initializes django

pydoc.cli()