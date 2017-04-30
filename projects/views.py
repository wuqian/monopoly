# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F, FloatField, Sum
from .models import *


# Create your views here.
def index(request):
    project_list = Project.objects.order_by('name')[:5];

    for project in project_list:
        project.receivable = project.contract_price * project.progress / Decimal(100.00)
        project.income = Record.objects.filter(value__gt = 0).aggregate(Sum('value'))['value__sum']
        project.expense = Record.objects.filter(value__lt = 0).aggregate(Sum('value'))['value__sum']

    context = {
        'project_list' : project_list
    }

    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    try:
        p = Project.objects.get(pk=project_id)
        stub_set_list = StubSet.objects.filter(project=p)
        for stub_set in stub_set_list:
            if (stub_set.finished_number != None):
                stub_set.progress = (stub_set.finished_number / stub_set.count * 100).quantize(Decimal('0.00'))
            else:
                stub_set.progress = 0
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    return render(request, "projects/detail.html", {'project' : p, "stub_set_list" : stub_set_list})
