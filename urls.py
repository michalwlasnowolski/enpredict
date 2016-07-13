from django.conf.urls import include, url, patterns
from . import views




urlpatterns = patterns('',

    url(r'vista', views.resources_vista),
    url(r'fly', views.resources_fly),
    url(r'compute_prediction', views.compute_prediction),
    url(r'compute', views.compute),
    url(r'mutate', views.mutate),
    url(r'spoil', views.spoil),
    url(r'download_wigfile', views.download_wigfile),
    url(r'^', views.index),
    


)

