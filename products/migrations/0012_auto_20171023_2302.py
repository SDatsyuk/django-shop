# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productimage_is_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='id_product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='propertyvalue',
            old_name='id_product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='propertyvalue',
            old_name='id_property',
            new_name='property',
        ),
    ]