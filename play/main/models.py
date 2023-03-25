from django.db import models

class Person(models.Model):
    user_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    weight = models.IntegerField()
    height = models.IntegerField()
    login = models.EmailField()
    password = models.CharField(max_length=20)
    point = models.IntegerField()
    power = models.IntegerField()
    health = models.IntegerField()
    skill = models.IntegerField()