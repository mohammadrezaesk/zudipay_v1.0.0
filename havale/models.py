from django.db import models

# Create your models here.
class tour(models.Model):
    tourleader = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    day = models.IntegerField(default=True)
    month = models.IntegerField(default=True)
    def __str__ (self):
        return self.tourleader
class traveler(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.IntegerField(default=True)
    birthmonth = models.IntegerField(default=True)
    birthyear = models.IntegerField(default=True)
    passport = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    ischild = models.BooleanField(default=False)
    touri = models.ForeignKey(tour, on_delete=models.CASCADE)
    def __str__(self):
        return self.touri.tourleader
