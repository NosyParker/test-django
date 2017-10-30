from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Meal,Customer
from .forms import UserForm

def home(request):
    random_meals = Meal.objects.order_by('?')[:4]
    return render(request, 'core_app/home.html', {'random_meals':random_meals})



def system_sign_up(request):
    if request.method=="POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            customer = user_form.save(commit=False)
            customer.user_name = request.POST['username']
            customer.phone = request.POST['phone']
            customer.address = request.POST['address']
            customer.save()

        
    else:
        user_form = UserForm()

    return render(request, 'core_app/sign_up.html', {'user_form':user_form})