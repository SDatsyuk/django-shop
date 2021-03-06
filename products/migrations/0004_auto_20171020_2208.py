# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171020_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='id_product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_property',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Property'),
        ),
        migrations.AddField(
            model_name='property',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
