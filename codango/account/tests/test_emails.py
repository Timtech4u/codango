from django.test import TestCase
from mock import patch
from account.emails import SendGrid
from account.tests.factories import ContactFactory


class EmailTestCase(TestCase):

    def setUp(self):
        contact = ContactFactory()
        self.email = SendGrid.compose(
            sender='Codango <codango@andela.com>',
            recipient=contact.email,
            subject='Codango: Password Recovery',
            text="This is a test",
            html=None,
        )

    # mock sendgrid send method when sending mails
    def test_send_email(self):
        with patch.object(SendGrid, 'send', return_value=200) as mock_method:
            response = mock_method(self.email)
            self.assertEquals(response, 200)
