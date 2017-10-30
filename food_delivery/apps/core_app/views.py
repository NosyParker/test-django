from django.shortcuts import render
from django.http import HttpResponse
from .models import Meal


def home(request):
    random_meals = Meal.objects.order_by('?')[:4]
    return render(request, 'core_app/home.html', {'random_meals':random_meals})