from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from community.models import AddOn


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


class TestAddOnViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test_user', password='test_password')
        self.user.set_password('test_password')
        self.user.save()
        self.login = self.client.login(
            username='test_user', password='test_password')

    def test_can_create_addon(self):
        data = {'name': 'Test_addon'}
        response = self.client.post(reverse('create_addon'), data)
        self.assertEqual(response.status_code, 200)

        # Test addon is created
        self.assertTrue(AddOn.objects.exists())
        self.assertTrue(AddOn.objects.filter(name='Test_addon'))

    def test_can_list_addons(self):
        self.addon_statistics = AddOn.objects.create(name="statistics")
        response = self.client.get(reverse('addon_list'))

        # Check if addon has been created. Change to relevant test after creating required views
        self.assertTrue(AddOn.objects.exists())
        self.assertTrue(AddOn.objects.filter(name="statistics"))

        self.assertEqual(len(response.context['addons']), 1)
        self.assertEqual(response.context['addons'][0], self.addon_statistics)
        self.assertEqual(response.status_code, 200)
