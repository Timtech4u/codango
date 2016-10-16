from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from resources.views import LoginRequiredMixin

from .forms import CommunityForm
from .models import Community, CommunityMember, AddOn


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
            CommunityMember.objects.create(community=community, user=self.request.user,
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


class CommunityListView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community_list.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityListView, self).get_context_data(**kwargs)
        context['communities'] = Community.objects.exclude(
            visibility='none')
        return context


class AddOnListView(LoginRequiredMixin, TemplateView):
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
