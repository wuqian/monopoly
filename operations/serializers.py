# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from operations.models import *

class MechineUsageRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mechine_id = serializers.IntegerField()
    op_id = serializers.IntegerField()
    from_stat_id = serializers.IntegerField()
    to_stat_id = serializers.IntegerField()

    def create(self, data):
        record = MechineUsageRecord.objects.create(**data)
        self.update_mechine_stat(record)
        return record

    def update(self, instance, data):
        instance.mechine = Mechine.objects.get(pk=data.mechine_id)
        instance.op = Operator.objects.get(pk=data.op_id)
        instance.from_stat = MechineStat.objects.get(pk=from_stat_id)
        instance.to_stat = MechineStat.objects.get(pk=to_stat_id)
        instance.save()
        return instance

    def update_mechine_stat(self, record):
        mechine = record.mechine
        stat = record.to_stat

        mechine.stat = stat
        mechine.save()

        #TODO: update operator's status

class TampingRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mechine_record_id = serializers.IntegerField()
    stub_id = serializers.IntegerField()
    serial_num = serializers.IntegerField()
    drop_offset = serializers.IntegerField()
    depth_offset  = serializers.IntegerField()
    consumption = serializers.IntegerField()
    def create(self, data):
        return TampingRecord.objects.create(**data)
