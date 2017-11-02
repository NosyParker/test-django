from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse
from .models import Meal, Customer
from django.contrib.auth import login, authenticate
from .forms import CustomerSignUpForm, RegistrationForm

from urllib.parse import urlparse
 
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .support_funcs import get_next_url

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


# def system_sign_in(request):
#     """ Вход в аккаунт """

class ELoginView(View):
 
    def get(self, request):
        # if the user is logged in, then do a redirect to the home page
        if auth.get_user(request).is_authenticated:
            return redirect('/')
        else:
            # Otherwise, form a context with the authorization form 
            # and we return to this page context.
            # It works, for url - /admin/login/ and for /accounts/login/ 
            context = create_context_username_csrf(request)
            return render_to_response('core_app/sign_in.html', context=context)
 
    def post(self, request):
        # having received the authorization request
        form = AuthenticationForm(request, data=request.POST)
 
        # check the correct form, that there is a user and he entered the correct password
        if form.is_valid():
            # if successful authorizing user
            auth.login(request, form.get_user())
            # get previous url
            next = urlparse(get_next_url(request)).path
            # and if the user of the number of staff and went through url /admin/login/
            # then redirect the user to the admin panel
            if next == '/admin/login/' and request.user.is_staff:
                return redirect('/admin/')
            # otherwise do a redirect to the previous page,
            # in the case of a / accounts / login / will happen is another redirect to the home page
            # in the case of any other url, will return the user to the url
            return redirect(next)
 
        # If not true, then the user will appear on the login page
        # and see an error message
        context = create_context_username_csrf(request)
        context['login_form'] = form
 
        return render_to_response('core_app/sign_in.html', context=context)
 
 
# helper method to generate a context csrf_token
# and adding a login form in this context
def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['login_form'] = AuthenticationForm
    return context