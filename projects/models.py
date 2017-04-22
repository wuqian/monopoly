# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProjectManager(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField(blank=True,null=True)
    finish_date = models.DateTimeField(blank=True,null=True)
    owner = models.ForeignKey(ProjectManager)
    contract_price = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)
    progress = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    def __unicode__(self):
        return self.name

class StubType(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class StubSet(models.Model):
    name = models.CharField(max_length=200)
    stub_type = models.ForeignKey(StubType, blank=True, null=True)
    project = models.ForeignKey(Project)
    length_from = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)
    length_to = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)
    diameter = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)
    count = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=0)
    finished_number = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=0)
    def __unicode__(self):
        return self.name
    
