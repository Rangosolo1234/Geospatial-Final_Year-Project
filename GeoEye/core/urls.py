# urls.py

from django.urls import path
from .views import voltage_chart, random_voltage
from . import views

urlpatterns = [
    # Your other paths...
    path('', voltage_chart, name='voltage_chart'),
    path('api/random-voltage/', random_voltage, name='random_voltage'),
]
