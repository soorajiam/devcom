from django.conf.urls import url
from . import views

urlpatterns = [
    url(( r'^$'), views.blog, name='blog'),
    url(( r'^(?P<pk>[0-9]+)$'), views.view, name='view'),
    url(( r'^me$'), views.me, name='me'),
    url(( r'^new$'), views.new, name='new'),
    url(( r'^new/process$'), views.newprocess, name='newprocess'),
    url((r'^post/(?P<pk>[0-9]+)/edit$'),views.edit,name='edit'),
    url((r'^post/(?P<pk>[0-9]+)/delete$'),views.PostDelete.as_view(),name='postdelete'),
    url(( r'^fuc$'), views.Profile.as_view(), name='blog'),
]
