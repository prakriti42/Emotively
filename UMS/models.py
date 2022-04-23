from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


pat= '[a-z0-9._]+@[a-z]+\.[a-z]{2,3}'

# creating a validator function
def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE ,  primary_key=True)
    email = models.EmailField(max_length=100 , blank=True )
    dp = models.ImageField(default='default.png', upload_to='profile_pics', null = True, blank = True)
    firstname  = models.CharField("First Name" , max_length=120 , null = True, blank = True)
    lastname  = models.CharField("Last Name" , max_length=120 , null = True, blank = True)
    #phoneNumberRegex = RegexValidator(regex = r"^?\d{10}$")
    contactNumber = PhoneNumberField( unique = True, null = True, blank = True)
    totalDetection = models.IntegerField(default=0 , null = True, blank = True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    
=======


class Users(models.Model):

    firstname  = models.CharField("First Name" , max_length=120)
    def __str__(self):
        return self.name
    
class UserDetails(models.Model):
    
    surname  = models.CharField("Last Name" , max_length=120)
    bio = models.TextField(blank=True)
    email = models.CharField("Email" , max_length=120)
    # contactNumber = PhoneNumberField()
    userSince = models.DateField()

>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
