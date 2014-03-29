from django.conf.urls import patterns, url

from contracts import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<contract_id>\d+)/$', views.detail),
    url(r'^create/$', views.create),
    url(r'^(?P<contract_id>\d+)/update$', views.update),
    url(r'^(?P<contract_id>\d+)/disable', views.disable),
    url(r'^(?P<contract_id>\d+)/enable', views.enable),
)