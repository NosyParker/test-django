from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Meal, Customer
from django.contrib.auth import login, authenticate
from .forms import CustomerSignUpForm, RegistrationForm


def home(request):
    """ Вывод рандомных блюд на главной странице """

    random_meals = Meal.objects.order_by('?')[:4]
    return render(request, 'core_app/home.html', {'random_meals':random_meals})



def system_sign_up(request):
    """ Регистрация нового пользователя """

    if request.method == 'POST':
        register = RegistrationForm(request.POST, prefix='register')
        user_profile = CustomerSignUpForm(request.POST, prefix='profile')

        if register.is_valid() and user_profile.is_valid():
            
            user = register.save(commit=False)
            user.set_password(register.cleaned_data['password'])
            user.save()
            
            usrprof = user_profile.save(commit=False)
            usrprof.user = user
            usrprof.save()


            return HttpResponse('Congrats!!!')
    
    else:
        userform = RegistrationForm(prefix='register')
        userprofileform = CustomerSignUpForm(prefix='profile')
        return render(request, 'core_app/sign_up.html', {'userform': userform, 'userprofileform': userprofileform})