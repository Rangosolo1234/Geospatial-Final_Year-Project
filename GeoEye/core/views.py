#This is where I creatye my vies
#from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Counties, Incidences, StudyArea, VoltageData, PowerLine
from django.core.serializers import serialize

def index(request):
    return render(request, 'index.html')
def counties_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type = 'json')
def powerlinephase(request):
    powerlines = serialize('geojson', PowerLine.objects.all())
    return HttpResponse(powerlines, content_type = 'json')

def voltage_data_chart(request):
    return render(request, 'voltage-chart.html')
