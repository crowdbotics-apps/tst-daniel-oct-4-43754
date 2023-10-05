from django.conf import settings
from django.db import models
class Car(models.Model):
    'Generated Model'
    brand = models.CharField(max_length=255,)
    model = models.CharField(max_length=255,)
    date = models.DateField()
