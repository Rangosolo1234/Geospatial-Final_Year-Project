from django.contrib import admin
from .models import Incidences, Counties, StudyArea, VoltageData, PowerLine
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
   list_display = ('name','location')
   
admin.site.register(Incidences, IncidencesAdmin)

class CountiesAdmin(LeafletGeoAdmin):
   list_display = ('objectid', 'county_nam')

admin.site.register(Counties, CountiesAdmin)

class StudyAreaAdmin(LeafletGeoAdmin):
    list_display = ('id', 'geom',)
    search_fields = ['id']

class PowerLineAdmin(LeafletGeoAdmin):
    list_display = ('id', 'geom',)
    search_fields = ['id']

admin.site.register(PowerLine, PowerLineAdmin)

admin.site.register(StudyArea, StudyAreaAdmin)

admin.site.register(VoltageData)