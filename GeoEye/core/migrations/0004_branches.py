# Generated by Django 4.2.11 on 2024-03-21 12:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cadastral_popupinfo_alter_cadastral_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('folderpath', models.CharField(max_length=254)),
                ('symbolid', models.BigIntegerField()),
                ('altmode', models.IntegerField()),
                ('base', models.FloatField()),
                ('clamped', models.IntegerField()),
                ('extruded', models.IntegerField()),
                ('snippet', models.CharField(max_length=254)),
                ('popupinfo', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Branchess',
            },
        ),
    ]