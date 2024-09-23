from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,SADUser



class newac(forms.ModelForm):
    class Meta:
        model=User
        fields=['num','name','phone','date','year']
        

class sadac(forms.ModelForm):
    class Meta:
        model=SADUser
        fields=['num','name','phone','date']

