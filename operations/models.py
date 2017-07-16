# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from projects.models import *

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
    from_stat = models.ForeignKey(MechineStat, related_name='from_stat')
    to_stat = models.ForeignKey(MechineStat, related_name='to_stat')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.op.name + ":" + self.mechine.info + ":"

class TampingRecord(models.Model):
    mechine_record = models.ForeignKey(MechineUsageRecord)
    stub = models.ForeignKey(Stub)

    # 时间戳
    timestamp = models.DateTimeField(auto_now_add=True)
    # 夯击次数
    serial_num = models.PositiveIntegerField(blank=True, null=True)
    # 落距
    drop_offset = models.DecimalField(blank=True, null=True, max_digits=20,
                    decimal_places=2)
    # 贯入度
    depth_offset = models.DecimalField(blank=True, null=True, max_digits=20,
                    decimal_places=2)
    # 填料量
    consumption = models.DecimalField(blank=True, null=True, max_digits=20,
                    decimal_places=2)

    def __unicode__(self):
        return self.stub.desc + ":" + str(self.serial_num)
