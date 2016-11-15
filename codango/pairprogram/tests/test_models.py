from django.test import TestCase, Client
from django.contrib.auth.models import User
from community.tests.factories import UserFactory
from pairprogram.models import Session


class TestPairProgram(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory_user = UserFactory()
        self.user = User.objects.create(
            username=self.factory_user.username.replace(' ', ''),
            email=self.factory_user.email,
            password=self.factory_user.password)
        self.client.login(
            username=self.user.username,
            password=self.user.password)
        self.session = Session.objects.create(
            initiator=self.user, session_name="A very Random session")

    def test_can_create_session(self):
        pair_session = Session.objects.create(
            initiator=self.user, session_name="SomeRandomSession")
        self.assertIsInstance(pair_session, Session)

    def test_can_read_a_session(self):
        pair_session = Session.objects.get(
            session_name="A very Random session")
        self.assertIsInstance(pair_session, Session)

    def test_can_update_a_session(self):
        pair_session = Session.objects.get(
            session_name="A very Random session")
        pair_session.session_name = "My new session name"
        pair_session.save()
        pair_session = Session.objects.get(session_name="My new session name")
        self.assertEquals("My new session name", pair_session.session_name)

    def test_can_delete_a_session(self):
        pair_session = Session.objects.get(
            session_name="A very Random session")
        pair_session.delete()
        self.assertFalse(Session.objects.all().exists())
