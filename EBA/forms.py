from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Location(forms.Form):
  location = forms.CharField(label='location',max_length=100)



class UserForm(forms.ModelForm):
  password=forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ('username','email', 'password',)


class CustomerForm(forms.ModelForm):
  confirm_password=forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = Customer
    fields = [      
      'confirm_password','gender'
    ]
