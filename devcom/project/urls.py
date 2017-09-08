from django.conf.urls import url
from . import views

urlpatterns = [
    url(( r'^$'), views.team, name='signup'),
    url(( r'^projects$'), views.projects, name='signup'),
    url(( r'^projects/addnew$'), views.addnew, name='signup'),
    url(( r'^projects/addprocess$'), views.addprocess, name='signup'),
    url(( r'^projects/team/(?P<p>[0-9]+)/(?P<u>[0-9]+)$'), views.teamprocess, name='signup'),
    url(( r'^projects/(?P<pk>[0-9]+)$'), views.projectview, name='signup'),
    url(( r'^projects/edit/(?P<pk>[0-9]+)/$'), views.projectedit.as_view(), name='signup'),
    url(( r'^projects/addupdate/(?P<pk>[0-9]+)/$'), views.addupdate, name='signup'),
    url(( r'^projects/addupdate/process$'), views.updateprocess, name='signup'),


]
