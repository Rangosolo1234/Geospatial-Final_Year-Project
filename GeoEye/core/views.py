#This is where I creatye my vies
#from django.http import Http404
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Counties, Incidences, StudyArea, VoltageData, PowerLine, Cadastral, Branches, Households
from django.core.serializers import serialize
import folium
from folium import plugins
import ee
#ee.Initialize()
#import geemap
#import geemap
#geemap.Initialize(project='ee-kipkiruisolomon19')

def index(request):
    return render(request, 'index.html')
def counties_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type = 'json')
def powerlinephase(request):
    powerlines = serialize('geojson', PowerLine.objects.all())
    return HttpResponse(powerlines, content_type = 'json')
def parcels(request):
    parcels = serialize('geojson', Cadastral.objects.all())
    return HttpResponse(parcels, content_type = 'json')
def branches(request):
    branches = serialize('geojson', Branches.objects.all())
    return HttpResponse(branches, content_type = 'json')
def households(request):
    households = serialize('geojson', Households.objects.all())
    return HttpResponse(households, content_type = 'json')
