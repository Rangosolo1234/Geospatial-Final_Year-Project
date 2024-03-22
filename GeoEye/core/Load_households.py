import os
from django.contrib.gis.utils import LayerMapping
from .models import Households

# Auto-generated `LayerMapping` dictionary for Households model
households_mapping = {
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}

#Defining the path where to find the shapefile data and load it to variable aoi_shp
households_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geodata', 'Households.shp'))

#This function loads the actual data(counties.shp) to the database
#It loads the data referring to the mapping aspect above(geom) and saves it in Counties model

def run(verbose=True):
    lm = LayerMapping(Households, households_shp, households_mapping, transform=False, encoding='iso-8859-1')
    #To save into our db
    lm.save(strict=True, verbose=verbose)