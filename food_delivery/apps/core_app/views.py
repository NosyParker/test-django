from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import TemplateView, FormView

from core_app.forms import UserRegistrationForm, UserUpdateProfileForm, CustomerUpdateProfileForm
from core_app.models import Customer
import food_delivery.settings as settings
import django.contrib.messages


def logout_required(view):
    def wrapper_func(request, *args, **kwargs):
        if not (request.user.is_authenticated):
            return view(request, *args, **kwargs)
        return redirect('core_app:home')
    return wrapper_func


@login_required(login_url = settings.LOGIN_URL)
@transaction.atomic
def account(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect (settings.ADMIN_STAFF_REDIRECT_URL)

    if request.method == "POST":
        user_profile_form = UserUpdateProfileForm(request.POST, instance=request.user)
        customer_profile_form = CustomerUpdateProfileForm(request.POST, instance=request.user.customer)
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


class HomeView(TemplateView):
    template_name = 'core_app/newed/base.html'


class SignUpView(FormView):

    template_name = 'core_app/sign_up.html'
    form_class = UserRegistrationForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        new_user = User.objects.create_user(**form.cleaned_data)
        new_customer = Customer.objects.create(user=new_user)
        new_customer.save()

        login(self.request, authenticate(
            username = form.cleaned_data["username"],
            password = form.cleaned_data["password"]
         ))

        return redirect(self.get_success_url())


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return render(request, 'core_app/sign_up.html', {"form":form})