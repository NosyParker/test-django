from django import forms

from django.contrib.auth.models import User
from core_app.models import Customer, Meal


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password=forms.CharField(label="Пароль", widget=forms.PasswordInput(), required=True)
    confirm_password=forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.pop("confirm_password", None)

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают!"
            )         
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = ("username", "email", "password")
        #exclude=["last_login", "user_permissions","is_staff","is_active","date_joined","groups","is_superuser"]
    

class UserUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class CustomerUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("phone", "address", )