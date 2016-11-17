from django.test import TestCase, Client

from account.models import ContactModel
from account.tests.factories import ContactFactory


class TestAccountProgram(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact = ContactFactory()

    def test_can_create_contact_instance(self):
        self.assertIsInstance(
            self.contact, ContactModel)

    def test_can_read_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            subject=self.contact.subject)
        self.assertIsInstance(contact_instance, ContactModel)

    def test_can_update_a_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            name=self.contact.name)
        contact_instance.name = "Jane Doe"
        contact_instance.save()
        contact_instance = ContactModel.objects.get(
            name="Jane Doe")
        self.assertEquals(
            self.contact.message,
            contact_instance.message)

    def test_can_delete_a_contact_instance(self):
        contact_instance = ContactModel.objects.get(
            name=self.contact.name)
        contact_instance.delete()
        self.assertFalse(ContactModel.objects.all().exists())
