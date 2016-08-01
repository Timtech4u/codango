from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.template import RequestContext, loader, Context
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import JsonResponse, QueryDict
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView, View

from account.emails import SendGrid
from pairprogram.forms import SessionForm
from pairprogram.models import Participant, Session
from pyfirebase import Firebase
from resources.views import LoginRequiredMixin


class StartPairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/sessions.html'
    form_class = SessionForm

    def post(self, request, **kwargs):
        form = self.form_class(
            request.POST, instance=request.user.profile)

        if form.is_valid():
            new_session = Session.objects.create(
                initiator=request.user,
                session_name=form.cleaned_data['session_name'])
            new_session.save()
            Participant.objects.create(
                participant=request.user, session_id=new_session.id)
            messages.add_message(
                request, messages.SUCCESS, 'Session started successfully')
            return redirect('/pair/' + str(new_session.id),
                            context_instance=RequestContext(request))


class ListSessionView(LoginRequiredMixin, TemplateView):
    form_class = SessionForm
    template_name = 'pairprogram/sessions.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListSessionView, self).get_context_data(**kwargs)
        participants = Participant.objects.filter(
            participant=self.request.user).all()

        sessions = []
        for participant in participants:
            sessions.append(participant.session)

        context['sessions'] = sessions
        context['sessionform'] = self.form_class()
        return context


class PairSessionView(LoginRequiredMixin, View):
    form_class = SessionForm
    template_name = 'pairprogram/editor.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['session_id'] = kwargs['session_id']
        participants = Participant.objects.filter(
            session_id=context['session_id']).all()

        result = any(self.request.user == row.participant
                     for row in participants)
        context['profile'] = self.request.user.profile
        context['session'] = Session.objects.get(
            id=context['session_id'])
        context['sessionform'] = self.form_class()
        context['themes'] = settings.EDITOR_THEME.iteritems()
        context['languages'] = settings.EDITOR_LANGUAGE.iteritems()

        if not result:
            messages.add_message(self.request, messages.ERROR,
                                 'No Access to this page')
            return redirect('/home',
                            context_instance=RequestContext(self.request))

        return render(request, self.template_name, context)

    def send_invites(self, email, session, request):
        user = User.objects.filter(email=email).first()
        if user is not None:
            try:
                Participant.objects.create(
                    participant=user, session=session)

            except IntegrityError:
                pass
            url = 'http://{}{}'.format(
                request.get_host(), reverse(
                    'pair_program', kwargs={'session_id': session.id}))
        else:
            url = 'http://{}{}?session_id={}'.format(
                request.get_host(), reverse('index'), session.id)

        email_context = {
            'subject': 'Let\'s Start Pairing now!',
            'url': url,
            'session_name': session.session_name
        }

        message = SendGrid.compose(
            sender='Codango-user {} <{}>'.format(
                request.user.username.upper(), request.user.email),
            recipient=email,
            subject="Join session in Codango",
            text=loader.get_template(
                'emails/session-invite.txt'
            ).render(Context(email_context)),
            html=loader.get_template(
                'emails/session-invite.html'
            ).render(Context(email_context))
        )
        # send email
        response = SendGrid.send(message)
        return response

    def post(self, request, *args, **kwargs):
        user_list = request.POST.getlist('userList[]')
        session = Session.objects.get(id=kwargs['session_id'])
        result = []
        for email in user_list:
            response_dict = {}
            response_dict['email'] = email
            response_dict['status'] = "error"
            if request.user.email != email:
                participants = Participant.objects.filter(session=session)
                if len(participants) < 5:
                    response = self.send_invites(email, session, request)
                    response_dict['message'] = "Successfully sent" \
                        if response == 200 else "There was an error"
                    response_dict['status'] = "success" \
                        if response == 200 else "error"
                else:
                    response_dict[
                        'message'] = "A session cannot hold more than 5 users"
            else:
                response_dict[
                    'message'] = "You can't send an invite to yourself"
            result.append(response_dict)
        return JsonResponse(
            {'response': result})

    def put(self, request, *args, **kwargs):
        data = QueryDict(request.body)
        language = data.get('language', 'python')
        session = Session.objects.get(id=kwargs['session_id'])
        response_dict = {}
        if session:
            session.language = language
            session.save()
            response_dict[
                'message'] = "Session updated successfully"
        else:
            response_dict[
                'message'] = "Session unable to updated"

        return JsonResponse(
            {'response': response_dict})


class DeleteSessionView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        session_id = request.POST['session_id']
        firebase = Firebase('https://project-8667655276128018284.fir'
                            'ebaseio.com/')
        pair_users_ref = "session/{}/users".format(session_id)
        pair_users_session = firebase.ref(pair_users_ref).child(session_id)

        try:
            session = Session.objects.get(id=session_id)
            if session.initiator == self.request.user:
                pair_users_session.delete()
                session.delete()
            else:
                participant = Participant.objects.filter(
                    session_id=session_id, participant_id=self.request.user)
                participant_id = self.request.user.id
                pair_users_session.child(str(participant_id)).delete()
                participant.delete()
        except Session.DoesNotExist:
            pass
        return JsonResponse({
            'status': 'success',
        }, status=200)
