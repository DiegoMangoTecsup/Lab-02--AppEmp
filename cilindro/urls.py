from django.urls import path
from .views import calcular_volumen

urlpatterns = [
    path('', calcular_volumen, name='calcular_volumen'),
]