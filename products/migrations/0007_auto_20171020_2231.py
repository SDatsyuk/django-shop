# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20171020_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='unit_of_measurement',
        ),
        migrations.AddField(
            model_name='propertyvalue',
            name='unit_of_measurement',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]
