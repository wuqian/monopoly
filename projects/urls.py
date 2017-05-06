from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^stubs/(?P<stub_id>[0-9]+)/$', views.stub_detail, name='stub_detail')
]
