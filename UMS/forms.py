from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=120, required=False)
    last_name = forms.CharField(max_length=120, required=False)
    email = forms.EmailField(max_length=120, required=False)
    totalDetections = forms.IntegerField(required=False)
    contactNumber = forms.CharField(max_length=10, required=False)
