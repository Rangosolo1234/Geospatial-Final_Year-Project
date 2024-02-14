#This is where I creatye my vies
#from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Counties, Incidences, StudyArea, VoltageData, PowerLine
from django.core.serializers import serialize
import folium
from folium import plugins
import ee

ee.Initialize()

def index(request):
    return render(request, 'index.html')
def counties_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type = 'json')
def powerlinephase(request):
    powerlines = serialize('geojson', PowerLine.objects.all())
    return HttpResponse(powerlines, content_type = 'json')

class home(TemplateView):
    template_name = 'index.html'

    # Define a method for displaying Earth Engine image tiles on a folium map.
    def get_context_data(self, **kwargs):

        figure = folium.Figure()
        
        #create Folium Object
        m = folium.Map(
            location=[28.5973518, 83.54495724],
            zoom_start=8
        )

        #add map to figure
        m.add_to(figure)

        
        #select the Dataset Here's used the MODIS data
        dataset = (ee.ImageCollection('MODIS/006/MOD13Q1')
                  .filter(ee.Filter.date('2019-07-01', '2019-11-30'))
                  .first())
        modisndvi = dataset.select('NDVI')

        #Styling 
        vis_paramsNDVI = {
            'min': 0,
            'max': 9000,
            'palette': [ 'FE8374', 'C0E5DE', '3A837C','034B48',]}

        
        #add the map to the the folium map
        map_id_dict = ee.Image(modisndvi).getMapId(vis_paramsNDVI)
       
        #GEE raster data to TileLayer
        folium.raster_layers.TileLayer(
                    tiles = map_id_dict['tile_fetcher'].url_format,
                    attr = 'Google Earth Engine',
                    name = 'NDVI',
                    overlay = True,
                    control = True
                    ).add_to(m)

        
        #add Layer control
        m.add_child(folium.LayerControl())
       
        #figure 
        figure.render()
         
        #return map
        return {"map": figure}