from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from resources.views import LoginRequiredMixin
from .forms import CommunityForm
from .models import Community, CommunityMember
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from resources.views import LoginRequiredMixin
from .forms import CommunityForm
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from community.models import CommunityMember, Community
from django.http import HttpResponse, HttpResponseNotFound


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
                return redirect('/community/{}'.format(kwargs.get(
                    'community_id')))
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
