from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestAddOns(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test_user', password='test_password')
        self.user.set_password('test_password')
        self.user.save()
        self.login = self.client.login(
            username='test_user', password='test_password')

    def test_create_addon_endpoint(self):
        response = self.client.get(reverse('create_addon'))
        self.assertEqual(response.status_code, 200)

    def test_addon_list_endpoint(self):
        response = self.client.get(reverse('addon_list'))
        self.assertEqual(response.status_code, 200)

    def test_addon_detail_endpoint(self):
        response = self.client.get(
            reverse('addon_detail', kwargs={'addon_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_access_create_addon_without_login(self):
        self.client.logout()
        response = self.client.get(reverse('create_addon'))
        self.assertEqual(response.status_code, 302)

    def test_access_list_addons_without_login(self):
        self.client.logout()
        response = self.client.get(reverse('addon_list'))
        self.assertEqual(response.status_code, 302)

    def test_access_addon_detail_without_login(self):
        self.client.logout()
        response = self.client.get(
            reverse('addon_detail', kwargs={'addon_id': 1}))
        self.assertEqual(response.status_code, 302)
