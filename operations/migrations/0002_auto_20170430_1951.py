# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechine',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.MechineStat'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.OperatorStat'),
        ),
    ]