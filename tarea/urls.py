from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tarea_list, name = 'tarea_list'),

    url(r'^tarea/(?P<pk>\d+)/$', views.tarea_detail, name = 'tarea_detail'),

    url(r'^tarea/(?P<pk>\d+)/edit/$', views.tarea_edit, name = 'tarea_edit'),

    url(r'^tarea/new/$', views.tarea_new, name = 'tarea_new'),
]
