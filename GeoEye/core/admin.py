from django.contrib import admin
from .models import Incidences

# Register your models here.
class IncidencesAdmin(admin.ModelAdmin):
   list_display = ('name','location')
   
admin.site.register(Incidences, IncidencesAdmin)