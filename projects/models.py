# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField(null=True)
    finish_date = models.DateTimeField(null=True)
    owner = models.CharField(max_length=200, blank=True)
