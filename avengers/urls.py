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

