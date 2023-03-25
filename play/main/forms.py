from django import forms
from .models import *

class PersonForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Имя игрока")
    sex = forms.CharField(max_length=10, label="Пол(m/w)")
    weight = forms.IntegerField(label="Вес")
    height = forms.IntegerField(label="Рост")
    login = forms.EmailField(label="Логин")
    password = forms.CharField(max_length=20, label="Пароль")
