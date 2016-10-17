from django.conf.urls import url
from resources import views

urlpatterns = [
    url(r'^(?P<resource_id>[0-9]+)/(?P<action>likes|unlikes)$',
        views.ResourceVoteView.as_view(), name='resource_vote'),
    url(r'^community/(?P<community_id>[0-9]+)/create$',
        views.CommunityView.as_view(), name='resource_create'),
    url(r'^create$',
        views.CommunityView.as_view(), name='resource_create'),
    url(r'^ajax/community/(?P<community>\w+|)$',
        views.CommunityView.as_view(), name='community'),
    url(r'^post/(?P<resource_id>[0-9]+)$',
        views.SinglePostView.as_view(), name='single_post'),
    url(r'^edit/(?P<resource_id>[0-9]+)$',
        views.ResourceEditView.as_view(), name='edit_post'),
]
