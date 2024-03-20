#This is where I set my routes for views
from django.urls import path  # this is the module that allows you to set the path to your url

from . import views # imports all the libraries that have been created in views file
urlpatterns = [
    path('', views.index, name = 'index'),
    path('counties_datasets', views.counties_datasets, name = 'KenyaCounties'),
    path('powerlinedata/', views.powerlinephase, name = 'powerlines'),
    path('parcels', views.parcels, name = 'Nyeriviewparcels'),
]