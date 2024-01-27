# views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import VoltageData
import random

def voltage_chart(request):
    return render(request, 'voltage_chart.html')

def random_voltage(request):
    if request.method == 'GET':
        voltage = random.uniform(0, 500)
        voltage_data = VoltageData.objects.create(value=voltage, timestamp=timezone.now())
        response_data = {
            'voltage': voltage_data.value,
            'timestamp': voltage_data.timestamp.strftime('%Y-%m-%dT%H:%M:%S'),
        }

        return JsonResponse(response_data)
