from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from core_app.forms import UserRegistrationForm, UserUpdateProfileForm, CustomerUpdateProfileForm
from core_app.models import Customer
import django.contrib.messages

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


def logout_required(view):
    def wrapper_func(request, *args, **kwargs):
        if not (request.user.is_authenticated):
            return view(request, *args, **kwargs)
        return redirect('core_app:home')
    return wrapper_func


@login_required(login_url='/sign-in')
@transaction.atomic
def account(request):
    if request.method == "POST":
        user_profile_form = UserUpdateProfileForm(request.POST,instance=request.user)
        customer_profile_form = CustomerUpdateProfileForm(request.POST,instance=request.user.customer)
        if user_profile_form.is_valid() and customer_profile_form.is_valid():
            user_profile_form.save()
            customer_profile_form.save()
            return redirect("core_app:account")
        else:
            messages.error(request, _('Исправьте ошибки!'))
    else:
        user_profile_form = UserUpdateProfileForm(instance=request.user)
        customer_profile_form = CustomerUpdateProfileForm(instance=request.user.customer)
    return render(request, 'core_app/account.html', {
                "user_profile_form": user_profile_form,
                "customer_profile_form":customer_profile_form
                })
