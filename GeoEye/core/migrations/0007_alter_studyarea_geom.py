# Generated by Django 5.0.1 on 2024-01-26 09:01

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_studyarea_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyarea',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]