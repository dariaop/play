from django.contrib import admin

from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'sex', 'weight', 'height', 'login', 'password')


admin.site.register(Person, PersonAdmin)