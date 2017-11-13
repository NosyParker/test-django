from django import forms

from django.contrib.auth.models import User
from core_app.models import Customer, Meal


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        #fileds = ["username", "password", "first_name", "last_name", "email",]
        exclude=["last_login", "user_permissions","is_staff","is_active","date_joined","groups","is_superuser"]
    


