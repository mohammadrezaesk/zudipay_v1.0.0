from django.db import models

# Create your models here.
class pricecard(models.Model):
    country = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    price = models.FloatField(max_length=30)
    ishow = models.BooleanField(default=True)
    def __str__ (self):
        return self.city
