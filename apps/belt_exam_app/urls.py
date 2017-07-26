from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'show/(?P<id>\d+)$', views.show_destination),
    url(r'add_destination/$', views.add_destination_page),
    url(r'process_destination$', views.process_destination),
    url(r'process_join/(?P<id>\d+)$', views.process_join),
]