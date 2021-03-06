# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 22:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexDinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner_name', models.CharField(max_length=140, verbose_name='Название')),
                ('cost', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('dinner_img', models.ImageField(upload_to='dinners_images/')),
            ],
            options={
                'verbose_name': 'Обед',
                'verbose_name_plural': 'Обеды',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=140, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=140, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cost', models.IntegerField(default=0, verbose_name='Цена')),
                ('category', models.CharField(choices=[('DRINKS', 'Напитки'), ('SALADS', 'Салаты'), ('SUSHI', 'Суши'), ('PIZZA', 'Пицца'), ('SNACKS', 'Закуски'), ('SOUPS', 'Супы'), ('MAIN_DISHES', 'Вторые блюда'), ('DESSERTS', 'Десерты')], max_length=20)),
                ('meal_img', models.ImageField(upload_to='meals_images/')),
                ('dinner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.ComplexDinner', verbose_name='Входит в состав обеда')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Новый заказ'), (2, 'В работе'), (3, 'завершен')], verbose_name='Статус заказа')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Customer', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Order')),
            ],
        ),
    ]
