from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView, View
from resources.views import LoginRequiredMixin

from .forms import AddOnForm, CommunityForm
from .models import AddOn, CommunityMember


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


class ListCreateAddOnView(LoginRequiredMixin, TemplateView):
    form_class = AddOnForm
    template_name = 'addon/addon_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListCreateAddOnView, self).get_context_data(**kwargs)
        addons = AddOn.objects.all()

        context['addons'] = addons
        context['addonform'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            addon = form.save()
            addon.save()
            messages.add_message(
                request, messages.SUCCESS, 'Addon created successfully')
            return redirect('/community/list_addons',
                            context_instance=RequestContext(request))

        else:
            messages.add_message(
                request, messages.ERROR, 'Addon not created. Please try again')
        return render(request, self.template_name, self.get_context_data())


class AddOnDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'addon/addon_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AddOnDetailView, self).get_context_data(**kwargs)
        addon_id = int(kwargs['addon_id'])
        addon = AddOn.objects.get(pk=addon_id)

        context['addon'] = addon
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class AddOnDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        addon_id = int(kwargs['addon_id'])
        addon = AddOn.objects.get(pk=addon_id)
        addon.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Addon deleted successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
