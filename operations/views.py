# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import *
from rest_framework.parsers import *


from .models import *
from .serializers import *
from projects.models import *
# Create your views here.
def index(request):
    operator_list = Operator.objects.all()
    mechine_list = Mechine.objects.all()
    usage_record_list = MechineUsageRecord.objects.all().order_by('-timestamp')
    stub_list = Stub.objects.all()

    context = {
        'operator_list' : operator_list,
        'mechine_list' : mechine_list,
        'usage_record_list' : usage_record_list,
        'stub_list' : stub_list
    }

    return render(request, 'operations/index.html', context)

@csrf_exempt
def create_usage_record(request):
    if request.method != 'POST':
        return JsonResponse({'deathrattle':'request method is not POST'}, status=400)

    data = JSONParser().parse(request)
    serializer = MechineUsageRecordSerializer(data=data)
    if (serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({'deathrattle':'data invalid'}, status=400)

@csrf_exempt
def create_tamping_record(request):
    if request.method != 'POST':
        return JsonResponse({'deathrattle':'request method is not POST'}, status=400)

    data = JSONParser().parse(request)
    serializer = TampingRecordSerializer(data=data)
    if (serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({'deathrattle':'data invalid'}, status=400)

def tamping_record_list(request, usage_id):
    usage_record = MechineUsageRecord.objects.get(pk=usage_id)
    tamping_record_list = TampingRecord.objects.filter(mechine_record=usage_record)
    context = {
        'tamping_record_list' : tamping_record_list
    }

    return JsonResponse(tamping_record_list, status=201)
#    return render(request, 'operations/tamping_record_list.html', context)

