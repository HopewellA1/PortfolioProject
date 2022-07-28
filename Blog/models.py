from email.mime import image
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title
