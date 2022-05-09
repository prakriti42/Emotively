from django.db import models
from django.db.models import Model 
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils import timezone

from datetime import datetime
# Create your models here.


class Audio_Storage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True) 
    # audio_file = models.FileField(
    #     storage=FileSystemStorage(location=settings.MEDIA_ROOT) , null=False , blank= False
    # )
    audio_file = models.FileField(upload_to="media/", null=True , blank=True)
    recordingname = models.CharField(default="Unknown",max_length=100 , null= False , blank = False)
    duration  = models.FloatField(default=0.0,null= False , blank = False)
    dateofUpload = models.DateField(null= False , blank = False)
    # timeToUpload = models.TimeField(null=True , blank=True)
    Tag = models.CharField(default="Untagged",max_length=10 , null= True , blank = True)

    def __str__(self):
        return str(self.recordingname)



