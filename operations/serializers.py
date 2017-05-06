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
        return MechineUsageRecord.objects.create(**data)

    def update(self, instance, data):
        instance.mechine = Mechine.objects.get(pk=data.mechine_id)
        instance.op = Operator.objects.get(pk=data.op_id)
        instance.from_stat = MechineStat.objects.get(pk=from_stat_id)
        instance.to_stat = MechineStat.objects.get(pk=to_stat_id)
        instance.save()

        return instance

