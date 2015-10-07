from django.conf import settings
from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^recovery/$', views.ForgotPassword.as_view(),
        name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$',
        views.ResetPassword.as_view(), name='reset_password'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^community/(?P<community>\w+)$',
        views.CommunityView.as_view(), name='community'),
    url(r'^user/(?P<username>\w+)$',
        views.UserProfileDetailView.as_view(), name='user_profile'),
    url(r'^user/(?P<username>\w+)/edit$',
        views.UserProfileEditView.as_view(), name='edit_user_profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
]
