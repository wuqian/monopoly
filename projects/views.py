# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    project_list = Project.objects.order_by('name')[:5];
    context = {
        'project_list' : project_list
    }
    return render(request, 'projects/index.html', context)
