from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.encoding import force_text
from django.views.generic import TemplateView

from .forms import CommunityForm
from .models import Community, CommunityMember, AddOn
from resources.views import LoginRequiredMixin


class UserPassesTestMixin(object):
    """
    CBV Mixin that allows you to define a test function which must return True
    if the current user can access the view.
    """

    login_url = reverse_lazy('login')
    permission_denied_message = 'You do not have permission to this resource'
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_login_url(self):
        """
        Override this method to override the login_url attribute.
        """
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
                '{0}.get_login_url().'.format(self.__class__.__name__)
            )
        return force_text(login_url)

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message

    def get_redirect_field_name(self):
        """
        Override this method to override the redirect_field_name attribute.
        """
        return self.redirect_field_name

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        raise PermissionDenied(self.get_permission_denied_message())

    def test_func(self):
        community = Community.objects.get(pk=self.kwargs.get('community_id'))
        return community.creator.id == self.request.user.id

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
        user_test_result = self.get_test_func()()
        if not user_test_result:
            return self.handle_no_permission()
        return super(UserPassesTestMixin, self).dispatch(request, *args, **kwargs)


class CommunityCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community-create.html'
    form_class = CommunityForm

    def dispatch(self, request, *args, **kwargs):
        return super(CommunityCreateView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommunityCreateView, self).get_context_data(**kwargs)
        context['community_form'] = CommunityForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            community = form.save(commit=False)
            community.creator = self.request.user
            community.save()
            CommunityMember.objects.create(
                community=community, user=self.request.user,
                invitor=self.request.user, status='approved',
                permission=community.default_group_permissions)
            return redirect(
                '/community/{}'.format(community.id)
            )

        else:
            context = super(CommunityCreateView,
                            self).get_context_data(*args, **kwargs)
            context['community_form'] = form
            return render(request, self.template_name, context)


class CommunityDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(**kwargs)
        try:
            context['community'] = Community.objects.get(
                id=kwargs.get('community_id'))
        except Community.DoesNotExist:
            raise Http404("Community does not exist")
        return context

    def post(self, request, *args, **kwargs):
        community = Community.objects.get(pk=kwargs.get('community_id'))
        members = CommunityMember.objects.get(user)
        context['community_name'] = Community.objects.get(
            pk=kwargs.get('community_id'))
        context['community_member'] = CommunityMember.objects.filter(
            community=context['community_id']).all()
        members = []
        for member in context['community_member']:
            members.append(str(member.user.username))
        if str(self.request.user) in members:
            context['member'] = True
            return context
        context['member'] = False
        return context

    def post(self, request, *args, **kwargs):
        community = Community.objects.get(pk=kwargs.get('community_id'))
        community_members = CommunityMember.objects.filter(
            community=community.id).all()
        member = []
        if community_members:
            for members in community_members:
                member.append(members.user.username)
            if str(self.request.user) in member:
                return redirect('/community/{}'.format(
                    kwargs.get('community_id')))
        if self.request.user and not community.private:
            new_member = CommunityMember(community=community,
                                         user=self.request.user,
                                         invitor=community.creator,
                                         status='approved')
            new_member.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Successfully joined ' + community.name + ' community!')
            return redirect('/community/{}'.format(kwargs.get('community_id')))
        else:

            if self.request.user and community.private:
                messages.add_message(
                    request, messages.SUCCESS,
                    'Successfully sent a join community request!')
                return redirect('/community/')


class CommunityListView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community_list.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityListView, self).get_context_data(**kwargs)
        context['communities'] = Community.objects.exclude(
            visibility='none')
        context['communities'] = Community.objects.all()
        context['communities'] = Community.objects.all()
        return context


class CommunityMemberListView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community_member_list.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityMemberListView,
                        self).get_context_data(**kwargs)
        context['community_members'] = CommunityMember.objects.all()
        return context


class AddOnListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'community/addon_list.html'

    def get_context_data(self, **kwargs):
        context = super(AddOnListView, self).get_context_data(**kwargs)
        community = Community.objects.get(
            id=kwargs.get('community_id'))
        context['addons'] = AddOn.objects.all()
        context['community_addons'] = community.addon_set.all()
        context['community_id'] = kwargs.get('community_id')
        return context

    def post(self, request, *args, **kwargs):
        checked_addons = request.POST.getlist('addons_check')
        community = Community.objects.get(
            id=kwargs.get('community_id'))
        addons = community.addon_set.all()
        for addon in addons:
            if addon not in checked_addons:
                community.addon_set.remove(addon)
        for addon_name in checked_addons:
            addon = AddOn.objects.get(name=addon_name)
            community.addon_set.add(addon)
        return redirect(
            '/community/{}'.format(community.id)
        )
