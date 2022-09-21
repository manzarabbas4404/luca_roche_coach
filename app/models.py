from ast import mod
from pyexpat import model
from django.db import models

# Create your models here.

class register(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)