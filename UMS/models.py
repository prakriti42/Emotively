from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

pat= '[a-z0-9._]+@[a-z]+\.[a-z]{2,3}'

# creating a validator function
def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE ,  primary_key=True)
    email = models.EmailField(max_length=100 , null = True , blank=True )
    dp = models.ImageField(default='all.JPG', storage = fs, null = True, blank = True)
    firstname  = models.CharField("First Name" , max_length=120 , null = True, blank = True)
    lastname  = models.CharField("Last Name" , max_length=120 , null = True, blank = True)
    #phoneNumberRegex = RegexValidator(regex = r"^?\d{10}$")
    contactNumber = PhoneNumberField( unique = True, null = True, blank = True)
    totalDetection = models.IntegerField(default = 0 , null = False, blank = False)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Messages(models.Model):
  
    sno = models.AutoField(primary_key=True)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.date}'

    
