from django import forms

from django.contrib.auth.models import User
from .models import Customer, Meal

class UserForm(forms.ModelForm):

    email = forms.CharField(max_length=140, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ("phone", "address")

