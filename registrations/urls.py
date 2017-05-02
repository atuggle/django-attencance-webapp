from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'registrataions'

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<event_id>[0-9]+)/export$', views.exportXlsx, name='exportXlsx'),
    url(r'^$', views.index, name='index'),
]

