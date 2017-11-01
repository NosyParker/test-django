from django import forms

from django.contrib.auth.models import User
from .models import Customer, Meal



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fileds=("email","username","first_name","last_name","password") ----так должно работать

        #но вместо этого приходится писать ----

        exclude=["last_login", "user_permissions","is_staff","is_active","date_joined","groups","is_superuser"] #ЭТОГО ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ


class CustomerSignUpForm(forms.ModelForm):

    class Meta:
        model = Customer
        # fields = ("phone","address") аналогично с верхней ситуацией
        exclude=["user"] # И ЭТОГО ТОЖЕ

