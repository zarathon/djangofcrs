from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mostrar/(?P<id>[0-9]+)$', views.mostrar_evento, name='mostrar_evento'),
]
