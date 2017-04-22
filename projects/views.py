# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    project_list = Project.objects.order_by('name')[:5];
    context = {
        'project_list' : project_list
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    try:
        p = Project.objects.get(pk=project_id)
        stub_set_list = StubSet.objects.filter(project=p)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, "projects/detail.html", {'project' : p, "stub_set_list" : stub_set_list})
