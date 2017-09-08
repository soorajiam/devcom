from django.conf.urls import url
from . import views

urlpatterns = [

    url(( r'^profile/edit$'), views.profileedit, name='signup'),
    url(( r'^profile/edit/verified/(?P<pk>[0-9]+)/$'), views.profEdit.as_view(), name='signup'),
    url(( r'^profile$'), views.profile, name='signup'),
    url(( r'^profile/(?P<pk>[0-9]+)$'), views.profileview, name='signup'),
    url(( r'^signup$'), views.signup, name='signup'),
    url(( r'^signupprocess$'), views.signupprocess, name='signupprocess'),
    url(( r'^login$'), views.login, name='login'),
    url(( r'^loginprocess$'), views.loginprocess, name='loginprocess'),

]
