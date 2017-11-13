from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core_app.forms import UserRegistrationForm
from core_app.models import Customer


@login_required(login_url='/sign-in')
def home(request):
    return render(request, 'core_app/home.html', {})


def sign_up(request):
    if request.method=="POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_customer = Customer.objects.create(user=new_user)
            new_customer.save()
            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))
            return redirect('core_app:home')
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'core_app/sign_up.html', {
            "user_form":user_form})
