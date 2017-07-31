from django.conf.urls import url
from . import views

urlpatterns = [
    url(( r'^$'), views.team, name='signup'),
    url(( r'^projects$'), views.projects, name='signup'),
    url(( r'^projects/(?P<pk>[0-9]+)$'), views.projectview, name='signup'),


]
