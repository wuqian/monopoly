# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_stubset_finished_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
