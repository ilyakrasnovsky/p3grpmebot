from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^$', views.index, name='index'),
	url(r'^behave/(?P<victimID>\d+)$', views.behave, name='behave'),
 	url(r'^start_the_fun/$', views.start_the_fun, name='start_the_fun'),
 	url(r'^end_the_fun/$', views.end_the_fun, name='end_the_fun'),
 	url(r'^activate_the_fun/$', views.activate_the_fun, name='activate_the_fun'),
 	url(r'^deactivate_the_fun/$', views.deactivate_the_fun, name='deactivate_the_fun'),	
]
