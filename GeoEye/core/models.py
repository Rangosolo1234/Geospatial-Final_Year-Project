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
    objectid = models.IntegerField()
    county_nam = models.CharField(max_length=50)
    count = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


    def __str__(self):
        return self.county_nam

    class Meta:
        verbose_name_plural ="Counties"
#Class model for Nyeri view my area of study
class StudyArea(models.Model):
    geom = models.PolygonField(srid=4326)
    name = models.CharField(max_length=50, default="Nyeri View")

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
    geom = models.MultiLineStringField(srid=4326)
    name = models.CharField(max_length=100, default='Phaseload')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Power line"


class Cadastral(models.Model):
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=250, null=True)
    popupinfo = models.CharField(max_length=250, null=True)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        #return f"Parcel ID: {self.id}, Source: {self.rim_source}, Parcel No: {self.parcel_no}"
        return self.name

    class Meta:
        verbose_name_plural = "Cadastrals"

    #Other fileds not much necessary
        
class Branches(models.Model):
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254, null=True)
    popupinfo = models.CharField(max_length=254, null=True)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Branchess"


class Households(models.Model):
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254, null=True)
    popupinfo = models.CharField(max_length=254, null=True)
    haslabel = models.IntegerField()
    labelid = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.name
    class meta:
        verbose_name_plural="Householdss"