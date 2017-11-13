# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class ComplexDinner(models.Model):
    dinner_name = models.CharField(max_length=140, verbose_name="Название")
    cost = models.IntegerField(default=0, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    dinner_img = models.ImageField(upload_to="dinners_images/", blank=False)


    def __str__(self):
        return self.dinner_name

    class Meta:
        verbose_name = "Обед"
        verbose_name_plural = "Обеды"


class Meal(models.Model):
    MEAL_CATEGORY = (
        ("DRINKS", "Напитки"),
        ("SALADS", "Салаты"),
        ("SUSHI", "Суши"),
        ("PIZZA", "Пицца"),
        ("SNACKS", "Закуски"),
        ("SOUPS", "Супы"),
        ("MAIN_DISHES", "Вторые блюда"),
        ("DESSERTS", "Десерты"),
    )
    dinner = models.ForeignKey(ComplexDinner, verbose_name="Входит в состав обеда", blank=True)
    meal_name = models.CharField(max_length=140, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.IntegerField(default=0, verbose_name="Цена")
    category = models.CharField(choices=MEAL_CATEGORY, max_length=20)
    meal_img = models.ImageField(upload_to="meals_images/", blank=False)


    def __str__(self):
        return self.meal_name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Customer(models.Model): 
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = models.CharField(max_length=140, verbose_name="Телефон", blank=True, null=True)
    address = models.CharField(max_length=500, verbose_name="Адрес", blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class Order(models.Model): 
    NEW_ORDER = 1
    WORKING = 2
    DONE = 3

    ORDER_STATUS = (
        (NEW_ORDER, 'Новый заказ'), (WORKING, 'В работе'), (DONE, 'завершен')
        )
    
    customer = models.ForeignKey(Customer, verbose_name="Заказчик")
    status = models.IntegerField(choices=ORDER_STATUS, verbose_name="Статус заказа")
    address = models.CharField(max_length=500, verbose_name="Адрес")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderDetails(models.Model): 
    order = models.ForeignKey(Order)
    meal = models.ForeignKey(Meal)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)