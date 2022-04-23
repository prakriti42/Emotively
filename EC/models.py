from django.db import models
from django.db.models import Model 
<<<<<<< HEAD
from django.contrib.auth.models import User

=======
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a

# Create your models here.

class Audio_Storage(models.Model):
<<<<<<< HEAD
    user= models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True) 
=======
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
    recording = models.FileField()
    duration  = models.FloatField()
    dateofUpload = models.DateField()
    timeToUpload = models.TimeField()
<<<<<<< HEAD
    Tag = models.CharField(max_length=10)

    def __str__(self):
        return self.recording.name


=======
    Owner = models.CharField(max_length=50)
    Tag = models.CharField(max_length=10)

>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a

