from django.conf.urls import include, url
from api import *

urlpatterns = [
    url(r'^tags$', views.TagView.as_view(), name='tag'),
    url(r'^tags/(?P<pk>\d+)/$', views.SingleTagView.as_view(), name='singletag'),

]