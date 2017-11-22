from django.contrib import admin
from .models import Meal, Order, ComplexDinner, Customer

admin.site.register(Order)
admin.site.register(Customer)

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'category', 'cost', 'dinner',)
    list_filter = ('category',)

@admin.register(ComplexDinner)
class ComplexDinnerAdmin(admin.ModelAdmin):
    list_display = ('dinner_name', 'cost',)

