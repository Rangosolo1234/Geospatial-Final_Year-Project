import os
from django.contrib.gis.utils import LayerMapping
from .models import Cadastral
cadastral_mapping = {
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}
#Defining the path where to find the shapefile data and load it to variable county_shp
Parcel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geodata','Nyeriparcels.shp'))

#This function loads the actual data(counties.shp) to the database
#It loads the data referring to the mapping aspect above(geom) and saves it in Counties model

def run(verbose=True):
    lm = LayerMapping(Cadastral, Parcel_shp, cadastral_mapping, transform=False, encoding='iso-8859-1')
    #To save into our db
    lm.save(strict=True, verbose=verbose)