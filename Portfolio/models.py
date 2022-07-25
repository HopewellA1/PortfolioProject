from email.mime import image
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Portfolio/images')
    url = models.URLField(blank=True)
    
    
    
