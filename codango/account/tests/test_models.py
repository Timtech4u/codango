from django.test import TestCase, Client
from account.models import ContactModel
from account.tests.factories import ContactFactory


class TestAccountProgram(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact_factory = ContactFactory.build()
        self.contact = ContactModel.objects.create(
            name=self.contact_factory.name,
            email=self.contact_factory.email,
            subject=self.contact_factory.subject,
            message=self.contact_factory.message,
            date_sent=self.contact_factory.date_sent)

    def test_can_create_contact_instance(self):
        self.assertIsInstance(
            self.contact_factory, ContactModel)

    def test_can_read_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            subject=self.contact_factory.subject)
        self.assertIsInstance(contact_instance, ContactModel)

    def test_can_update_a_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            name=self.contact_factory.name)
        contact_instance.name = "Jane Doe"
        contact_instance.save()
        contact_instance = ContactModel.objects.get(
            name="Jane Doe")
        self.assertEquals(
            self.contact_factory.message,
            contact_instance.message)

    def test_can_delete_a_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            name=self.contact_factory.name)
        contact_instance.delete()
        self.assertFalse(ContactModel.objects.all().exists())
