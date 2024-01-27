#from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="Incidences"

#Class model for data for kenya counties
class Counties(models.Model):
    objectid = models.AutoField(primary_key=True, default=0)
    county_nam = models.CharField(max_length=50)
    count = models.FloatField(default=0)
    shape_leng = models.FloatField(default=0)
    shape_area = models.FloatField(default=0)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural ="Counties"
#Class model for Nyeri view my area of study
class StudyArea(models.Model):
    #name = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "StudyArea"

class VoltageData(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"VoltageData(value={self.value}, timestamp={self.timestamp})"
    
    class Meta:
        verbose_name_plural = "VoltageData"

class PowerLine(models.Model):
    geom = models.LineStringField(srid=4326)

    #Other fileds not much necessary