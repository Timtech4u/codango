from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from account.views import ForgotPasswordView, ResetPasswordView
from mock import patch
from account.emails import SendGrid
from account.tests.factories import ContactFactory
from community.tests.factories import UserFactory
from resources.models import Resource
from pairprogram.models import Session, Participant


class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.created_factory_user = UserFactory.build_batch(2)
        self.created_factory_user_details, \
            self.created_factory_user2_details = \
            ContactFactory.build(name=self.created_factory_user[0].username), \
            ContactFactory.build(name=self.created_factory_user[1].username)
        User.objects.create_user(
            username=self.created_factory_user[0].username,
            password=self.created_factory_user[0].password,
        )
        self.initiator = User.objects.create_user(
            username=self.created_factory_user[1].username,
            password=self.created_factory_user[1].password,
            email=self.created_factory_user2_details.email
        )
        self.pair_session = Session.objects.create(
            id=1, initiator=self.initiator,
            session_name="SomeRandomSession")

    def test_can_reach_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_index_is_returned(self):
        match = resolve('/')
        self.assertEqual(match.url_name, 'index')

    def test_can_login(self):
        response = self.client.post('/login', {
            'username': self.created_factory_user[0].username,
            'password': self.created_factory_user[0].password
        })
        self.assertEqual(response.status_code, 302)

    def test_can_register(self):
        response = self.client.post('/register', {
            'username': self.created_factory_user[1].username.replace(' ', ''),
            'password': self.created_factory_user[1].password,
            'password_conf': self.created_factory_user[1].password,
            'email': self.created_factory_user2_details.email
        })
        self.assertEqual(response.status_code, 302)

    def test_can_register_and_create_session(self):
        response = self.client.post('/register', {
            'username': self.created_factory_user[1].username.replace(' ', ''),
            'password': self.created_factory_user[1].password,
            'password_conf': self.created_factory_user[1].password,
            'session_id': 1,
            'email': self.created_factory_user2_details.email
        })
        session_program = Participant.objects.all()
        self.assertEqual(len(session_program), 1)
        self.assertEqual(response.status_code, 302)


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.created_factory_user = UserFactory()
        self.user = User.objects.create_user(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password
        )
        self.user.set_password(self.created_factory_user.password)
        self.user.save()
        self.login = self.client.login(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password)

    def test_can_reach_home_page(self):
        self.assertEqual(self.login, True)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_home_is_returned(self):
        match = resolve('/home')
        self.assertEqual(match.url_name, 'home')


class SearchViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.created_factory_user = UserFactory()
        self.user = User.objects.create_user(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password
        )
        self.user.set_password(self.created_factory_user.password)
        self.user.save()
        self.login = self.client.login(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password)

    def create_resources(self, text='some more words',
                         resource_file='resource_file'):
        return Resource.objects.create(
            text=text, author=self.user, resource_file=resource_file
        )

    def test_can_reach_search_page(self):
        self.assertEqual(self.login, True)
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_can_search_based_on_user_or_resource(self):
        self.create_resources()
        self.create_resources()
        url = reverse('search_by', kwargs={'searchby': 'resources'})
        url2 = reverse('search_by', kwargs={'searchby': 'users'})

        response = self.client.get(url)
        response2 = self.client.get(url2)

        self.assertEqual(len(response.context['resources']), 2)
        self.assertEqual(len(response.context['users']), 2)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response.status_code, 200)

    def test_return_no_user_or_response_when_not_resource_is_found(self):
        self.create_resources()
        self.create_resources()
        url = reverse('search_by', kwargs={'searchby': 'resources'})
        url2 = reverse('search_by', kwargs={'searchby': 'users'})

        response = self.client.get(url + "?q=eaiofaowfjieaowef")
        response2 = self.client.get(url2 + "?q=eaiofaowfjieaowef")

        self.assertEqual(len(response.context['resources']), 0)
        self.assertEqual(len(response.context['users']), 0)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response.status_code, 200)


class ForgotResetTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_forgot_route_resolves_to_correct_view(self):
        response = self.client.get('/recovery')
        self.assertEqual(
            response.resolver_match.func.__name__,
            ForgotPasswordView.as_view().__name__)

    def test_reset_route_resolves_to_correct_view(self):
        response = self.client.get(
            '/recovery/ajkzfYba9847DgJ7wbkwAaSbkTjUdawGG998qo3HG8qae83')
        self.assertEqual(
            response.resolver_match.func.__name__,
            ResetPasswordView.as_view().__name__)


class PasswordResetTestCase(TestCase):

    def setUp(self):
        # create a test client:
        self.client = Client()
        # register a sample user:
        self.created_factory_user = UserFactory()
        self.created_factory_user_details = ContactFactory(
            name=self.created_factory_user.username)
        self.user_account = User.objects.create_user(
            self.created_factory_user.username.replace(' ', ''),
            self.created_factory_user_details.email,
            'codango')
        self.user_account.first_name = \
            self.created_factory_user.username.split(" ")[0]
        self.user_account.last_name = \
            self.created_factory_user.username.split(" ")[:1]
        self.user_account.save()

    def test_get_returns_200(self):
        response = self.client.get('/recovery')
        self.assertEquals(response.status_code, 200)

    def test_recovery_email_not_sent_for_unregistered_user(self):
        response = self.client.post(
            '/recovery', {"email": "fagemaki.iniruto@gmail.com"})
        self.assertNotIn('email_status', response.context)


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.created_factory_user = UserFactory()
        self.user = User.objects.create_user(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password
        )
        self.user.set_password(self.created_factory_user.password)
        self.user.save()
        self.login = self.client.login(
            username=self.created_factory_user.username.replace(' ', ''),
            password=self.created_factory_user.password)

    def test_can_reach_profile_page(self):
        response = self.client.get(
            '/user/{}'.format(
                self.created_factory_user.username.replace(' ', '')))
        self.assertEqual(response.status_code, 200)

    def test_can_reach_profile_edit_page(self):
        response = self.client.post(
            '/user/lade/edit',
            {
                'position': 'Software Developer',
                'place_of_work': 'Andela',
                'first_name': self.created_factory_user.username.split(" ")[0],
                'last_name': self.created_factory_user.username.split(" ")[:1],
                'about': 'I love to Code'
            })
        self.assertEqual(response.status_code, 302)
