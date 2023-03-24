from django.urls import path


from .views import *

urlpatterns = [
    path('', begin, name='begin'),
    path('main/', main, name='main'),
    path('play/', play, name='play'),
    path('career/', career, name='career'),
    path('training', training, name='training'),
    path('create/', create, name='create')
]