# Generated by Django 4.0.3 on 2022-03-07 08:48

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mh_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mh_tb',
            name='shape_wkt',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
    ]
