# Auto-generated `LayerMapping` dictionary for Counties model
import os
from django.contrib.gis.utils import LayerMapping
from .models import PowerLine

# Auto-generated `LayerMapping` dictionary for StudyArea model
powerline_mapping = {
    'geom': 'MULTILINESTRING25D',
    #'name': 'name'
}
#Defining the path where to find the shapefile data and load it to variable aoi_shp
powerline_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Powerline', 'Powerline.shp'))

#This function loads the actual data(counties.shp) to the database
#It loads the data referring to the mapping aspect above(geom) and saves it in Counties model

def run(verbose=True):
    lm = LayerMapping(PowerLine, powerline_shp, powerline_mapping, transform=False, encoding='iso-8859-1')
    #To save into our db
    lm.save(strict=True, verbose=verbose)