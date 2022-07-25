from email.mime import image
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    date = models.DateField()
    
