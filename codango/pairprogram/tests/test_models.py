from django.test import TestCase, Client

from community.tests.factories import UserFactory
from pairprogram.tests.factories import SessionFactory
from pairprogram.models import Session


class TestPairProgram(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.client.login(
            username=self.user.username,
            password=self.user.password)
        self.factory_session = SessionFactory(
            initiator=self.user)

    def test_can_create_session(self):
        self.assertIsInstance(self.factory_session, Session)

    def test_can_read_a_session(self):
        pair_session = Session.objects.get(
            session_name=self.factory_session.session_name)
        self.assertIsInstance(pair_session, Session)

    def test_can_update_a_session(self):
        pair_session = Session.objects.get(
            session_name=self.factory_session.session_name)
        pair_session.session_name = "My new session name"
        pair_session.save()
        pair_session = Session.objects.get(session_name="My new session name")
        self.assertEquals("My new session name", pair_session.session_name)

    def test_can_delete_a_session(self):
        pair_session = Session.objects.get(
            session_name=self.factory_session.session_name)
        pair_session.delete()
        self.assertFalse(Session.objects.all().exists())
