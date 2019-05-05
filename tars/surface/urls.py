from django.conf.urls import url

from tars.surface import views


urlpatterns = [
    url(r'^$', views.index, name='surface_index'),
    url(r'^ping/$', views.ping, name='surface_ping'),
    url(r'^settings/$', views.export_settings, name='settings'),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
]
