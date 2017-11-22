from django.contrib import admin
from .models import Meal, Order, ComplexDinner, Customer
from django.utils.html import format_html


admin.site.register(Order)
admin.site.register(Customer)

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('meal_name', 'category', 'cost', 'dinner', 'meal_image_thumbnail',)


@admin.register(ComplexDinner)
class ComplexDinnerAdmin(admin.ModelAdmin):
    list_display = ('dinner_name', 'cost',)

