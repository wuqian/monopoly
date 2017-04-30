# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class OperatorStat(models.Model):
    desc = models.CharField(max_length=200)
    def __unicode__(self):
        return self.desc

class Operator(models.Model):
    name = models.CharField(max_length=200)
    stat = models.ForeignKey(OperatorStat)
    def __unicode__(self):
        return self.name

class MechineStat(models.Model):
    desc = models.CharField(max_length=200)
    def __unicode__(self):
        return self.desc

class Mechine(models.Model):
    info = models.CharField(max_length=200)
    stat = models.ForeignKey(MechineStat)
    def __unicode__(self):
        return self.info

class MechineUsageRecord(models.Model):
    mechine = models.ForeignKey(Mechine)
    op = models.ForeignKey(Operator)
    from_stat = models.IntegerField()
    to_stat = models.IntegerField()
    def __unicode__(self):
        return self.op.name + ":" + self.mechine.info + ":"
