
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from UMS.models import Profile

class ProfileForm(ModelForm):
         class Meta:
            model = Profile 
            fields = (
                 'firstname',
                 'lastname',
                 'email',
                 'contactNumber',
                 'totalDetection',
                )

# class ProfileForm(ModelForm):
#          class Meta:
#          model = UserProfile
#          fields = ('city', 'description', 'phoneNumber', 'website', 'image') #Note that we didn't mention user field here.