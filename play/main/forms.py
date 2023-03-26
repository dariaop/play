from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['user_name', 'sex', 'weight', 'height', 'login', 'password']