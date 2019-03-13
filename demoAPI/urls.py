from django.contrib import admin
from django.urls import path

from . import views

app_name = 'demoAPI'

urlpatterns = [
    path('', views.index, name='index'),
    path('(<avenger_name>)', views.detail, name='detail'),
]
