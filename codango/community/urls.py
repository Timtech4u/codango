from community import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.CommunityListView.as_view(), name='community_list'),
    url(r'^create$',
        views.CommunityCreateView.as_view(), name='community_create'),
    url(r'^(?P<community_id>[0-9]+)$',
        views.CommunityDetailView.as_view(), name='community_detail'),
    url(r'^addon_list/(?P<community_id>[0-9]+)$',
        views.AddOnListView.as_view(), name='addon_list'),
]
