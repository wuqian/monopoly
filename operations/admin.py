# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(OperatorStat)
admin.site.register(Operator)
admin.site.register(MechineStat)
admin.site.register(Mechine)
admin.site.register(MechineUsageRecord)
