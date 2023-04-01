from django.urls import path

from . import views

app_name = 'formulario1'

urlpatterns = [
    path('', views.calcular, name='calcular'),
]