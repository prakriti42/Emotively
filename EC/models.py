from django.db import models
from django.db.models import Model 

# Create your models here.

class Audio_Storage(models.Model):
    recording = models.FileField()
    duration  = models.FloatField()
    dateofUpload = models.DateField()
    timeToUpload = models.TimeField()
    Owner = models.CharField(max_length=50)
    Tag = models.CharField(max_length=10)


