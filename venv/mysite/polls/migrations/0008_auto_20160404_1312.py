# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160404_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Preise', to='polls.Product_id'),
        ),
    ]
