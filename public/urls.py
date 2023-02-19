from django.urls import path

from .views import *

app_name = 'public'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('calcular_precio/', calcular_precio, name='calcular_precio'),
]