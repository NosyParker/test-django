from django.contrib import admin
from .models import Meal, Order, OrderDetails

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)