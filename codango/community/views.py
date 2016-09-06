from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from resources.views import LoginRequiredMixin

from .forms import CommunityForm
from .models import CommunityMember


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


class CommunityListView(LoginRequiredMixin, TemplateView):
    template_name = 'community/community_list.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityListView, self).get_context_data(**kwargs)
        context['communities'] = Community.objects.exclude(
            visibility='none')
        return context
