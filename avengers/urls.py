from django.contrib import admin
from django.urls import path

from . import views

app_name = 'avengers'


urlpatterns = [
    path('', views.index, name='index'),
    path('<avenger_name>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    # path('', views.create, name='create'),
]

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('(?P<slug>[\w-]+)$', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>', views.DeleteView.as_view(), name='delete'),
# ]
