# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    operator_list = Operator.objects.all()
    mechine_list = Mechine.objects.all()

    context = {
        'operator_list' : operator_list,
        'mechine_list' : mechine_list
    }

    return render(request, 'operations/index.html', context)
