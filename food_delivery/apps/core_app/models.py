from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html

class ComplexDinner(models.Model):
    dinner_name = models.CharField(max_length=140, verbose_name="Название")
    cost = models.IntegerField(default=0, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    dinner_img = models.ImageField(upload_to="dinners_images/", verbose_name="Изображение", blank=False)

    def __str__(self):
        return self.dinner_name

    class Meta:
        verbose_name = "Обед"
        verbose_name_plural = "Обеды"


class Meal(models.Model):
    MEAL_CATEGORY = (
        ("DRINKS", "Напитки"),
        ("SALADS", "Салаты"),
        ("SUSHI", "Суши/Роллы"),
        ("PIZZA", "Пицца"),
        ("SNACKS", "Закуски"),
        ("SOUPS", "Супы"),
        ("MAIN_DISHES", "Вторые блюда"),
        ("DESSERTS", "Десерты"),
    )
    dinner = models.ForeignKey(ComplexDinner, verbose_name="Входит в состав обеда", blank=True, null=True)
    meal_name = models.CharField(max_length=140, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.IntegerField(default=0, verbose_name="Цена")
    category = models.CharField(choices=MEAL_CATEGORY, max_length=20, verbose_name="Категория")
    meal_img = models.ImageField(upload_to="meals_images/", verbose_name="Изображение", blank=False)


    def __str__(self):
        return self.meal_name

    def meal_image_thumbnail(self):
        if self.meal_img:
            return format_html('<img src="{}" width="100" height="80" />'.format(self.meal_img.url))
        else:
            return "Изображение еще не добавлено"

    meal_image_thumbnail.allow_tags = True
    meal_image_thumbnail.short_description = 'Изображение'

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
    created_at_time = models.DateTimeField(default = timezone.now, verbose_name="Время заказа")
    delivered_at_time = models.DateTimeField(blank = True, null = True, verbose_name="Время доставки")

    def __str__(self):
        return str(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ("-created_at_time",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderDetails(models.Model): 
    order = models.ForeignKey(Order, verbose_name="Заказ")
    cost = models.IntegerField(null=True)
    quantity = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return str(self.id)

    def get_subtotal_cost(self):
        return self.quantity * self.cost

    class Meta:
        verbose_name = "Детали заказа"
        verbose_name_plural = "Детали заказа"