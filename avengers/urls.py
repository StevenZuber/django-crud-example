from django.contrib import admin
from django.urls import path

from . import views

app_name = 'avengers'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/(?P<slug>[\w-]+)/$>', views.DetailView.as_view(), name='detail'),
    path('/<int:pk>', views.DeleteView.as_view(), name='delete'),
]
