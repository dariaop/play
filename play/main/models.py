from django.db import models

class Person(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='Имя игрока')
    sex = models.CharField(max_length=10, verbose_name='Пол')
    weight = models.IntegerField(verbose_name='Вес')
    height = models.IntegerField(verbose_name='Рост')
    login = models.EmailField(verbose_name='Логин')
    password = models.CharField(max_length=20, verbose_name='Пароль')
