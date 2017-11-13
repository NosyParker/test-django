from django.contrib import admin
from .models import Meal, Order, ComplexDinner, Customer

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(ComplexDinner)
admin.site.register(Customer)