from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class adminpaneluser(models.Model):
    username = models.CharField(max_length = 30 ,default='',unique=True)
    password = models.CharField(max_length = 30 ,default='')
    def __str__(self):
        return self.username
