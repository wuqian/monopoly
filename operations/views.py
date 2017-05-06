# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.renderers import *
from rest_framework.parsers import *


from .models import *
from .serializers import *

# Create your views here.
def index(request):
    operator_list = Operator.objects.all()
    mechine_list = Mechine.objects.all()
    usage_record_list = MechineUsageRecord.objects.all()

    context = {
        'operator_list' : operator_list,
        'mechine_list' : mechine_list,
        'usage_record_list' : usage_record_list
    }

    return render(request, 'operations/index.html', context)

def create_usage_record(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MechineUsageRecordSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({'errors' : 'errors'}, status=400)
    else:
        return JsonResponse({'deathrattle':'request method is not POST'}, status=400)
