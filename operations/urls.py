from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^usage_record/$', views.create_usage_record),
    url(r'^tamping_record/$', views.create_tamping_record)
]
