from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model): # модель - "Блюдо/Обед"
    meal_name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.meal_name


class Customer(models.Model): #модель - "Заказчик"
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=140, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)


class Order(models.Model): #модель - "Заказ"
    NEW_ORDER = 1
    WORKING = 2
    DONE = 3

    ORDER_STATUS = (
        (NEW_ORDER, 'Новый заказ'), (WORKING, 'В работе'), (DONE, 'завершен')
        )
    
    customer = models.ForeignKey(Customer)
    status = models.IntegerField(choices=ORDER_STATUS)
    address = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)

class OrderDetails(models.Model): #модель - "Детализация заказа"
    order = models.ForeignKey(Order)
    meal = models.ForeignKey(Meal)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)