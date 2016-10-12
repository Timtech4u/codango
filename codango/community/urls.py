from community import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.CommunityListView.as_view(), name='community_list'),
    url(r'^create$',
        views.CommunityCreateView.as_view(), name='community_create'),
    url(r'^(?P<community_id>[0-9]+)$',
        views.CommunityDetailView.as_view(), name='community_detail'),
    url(r'^(?P<community_id>[0-9]+)/members$',
        views.CommunityMemberListView.as_view(), name='community_member'),
    url(r'^create_addon$',
        views.AddOnCreateView.as_view(), name='create_addon'),
    url(r'^list_addons$',
        views.AddOnListView.as_view(), name='addon_list'),
    url(r'^list_addons/(?P<addon_id>[0-9]+)$',
        views.AddOnDetailView.as_view(), name='addon_detail'),
]
