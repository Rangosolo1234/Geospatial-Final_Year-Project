from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
#from leaflet import app_settings, PLUGINS, PLUGIN_FORMS
from .models import Incidences, Counties, StudyArea, VoltageData, PowerLine, Cadastral, Branches, Households
#from django.contrib.gis.db import OSMGeoAdmin

class IncidencesAdmin(LeafletGeoAdmin):
   list_display = ('name','location')
   
admin.site.register(Incidences, IncidencesAdmin)

class CountiesAdmin(LeafletGeoAdmin):
   list_display = ('county_nam', 'count', 'shape_area', 'objectid')

admin.site.register(Counties, CountiesAdmin)

class StudyAreaAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geom')
    search_fields = ['name']

class PowerLineAdmin(LeafletGeoAdmin):
    list_display = ['name','id']
    search_fields = ['name']

class CadastralAdmin(LeafletGeoAdmin):
    list_display=['symbolid', 'shape_leng', 'shape_area']
    #search_fields=['symbolid']
class BranchesAdmin(LeafletGeoAdmin):
    list_display=['name', 'symbolid', 'shape_leng']

class HouseholdsAdmin(LeafletGeoAdmin):
    list_display=["name","symbolid"]

admin.site.register(PowerLine, PowerLineAdmin)

admin.site.register(StudyArea, StudyAreaAdmin)

admin.site.register(VoltageData)
admin.site.register(Cadastral, CadastralAdmin)
admin.site.register(Branches, BranchesAdmin)
admin.site.register(Households, HouseholdsAdmin)