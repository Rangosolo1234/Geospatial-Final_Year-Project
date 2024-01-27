# Auto-generated `LayerMapping` dictionary for Counties model
import os
from django.contrib.gis.utils import LayerMapping
from .models import StudyArea

# Auto-generated `LayerMapping` dictionary for StudyArea model
studyarea_mapping = {
    'geom': 'POLYGON25D',
}

#Defining the path where to find the shapefile data and load it to variable aoi_shp
aoi_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'aoi', 'NyeriView.shp'))

#This function loads the actual data(counties.shp) to the database
#It loads the data referring to the mapping aspect above(geom) and saves it in Counties model

def run(verbose=True):
    lm = LayerMapping(StudyArea, aoi_shp, studyarea_mapping, transform=False, encoding='iso-8859-1')
    #To save into our db
    lm.save(strict=True, verbose=verbose)