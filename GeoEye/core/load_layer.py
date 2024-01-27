# Auto-generated `LayerMapping` dictionary for Counties model
import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties
counties_mapping = {
    'objectid': 'OBJECTID',
    'county_nam': 'COUNTY_NAM',
    'count': 'COUNT',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

#Defining the path where to find the shapefile data and load it to variable county_shp
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geodata','Counties.shp'))

#This function loads the actual data(counties.shp) to the database
#It loads the data referring to the mapping aspect above(geom) and saves it in Counties model

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    #To save into our db
    lm.save(strict=True, verbose=verbose)
    