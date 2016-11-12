from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^$', views.index, name='index'),
	url(r'^behave/(?P<victimID>\d+)/', views.behave, name='behave'),
 	url(r'^boobot_ilya$', views.boobot_ilya, name='boobot_ilya'),
 	url(r'^boobot_dorothy$', views.boobot_dorothy, name='boobot_dorothy'),	
 	url(r'^start_the_fun$', views.start_the_fun, name='start_the_fun'),
 	url(r'^end_the_fun$', views.end_the_fun, name='end_the_fun'),
]
