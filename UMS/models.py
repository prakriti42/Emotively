from django.db import models


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

