from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Pictures

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']