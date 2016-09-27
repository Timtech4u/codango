from django.contrib.auth.models import User
from django.test import TestCase


class TestAddOns(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test_user', password='test_password')
        self.user.set_password('test_password')
        self.user.save()
        self.login = self.client.login(
            username='test_user', password='test_password')

    def test_create_addon_endpoint(self):
        """Test that users can create addon"""
        self.assertTrue(self.login)
        response = self.client.get('/community/create_addon')
        self.assertEqual(response.status_code, 200)

    def test_addon_list_endpoint(self):
        self.assertTrue(self.login)
        response = self.client.get('/community/list_addons')
        self.assertEqual(response.status_code, 200)

    def test_addon_detail_endpoint(self):
        self.assertTrue(self.login)
        response = self.client.get('/community/list_addons/1')
        self.assertEqual(response.status_code, 200)
