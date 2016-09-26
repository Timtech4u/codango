from community.models import Community, CommunityMember
from django.contrib.auth.models import User
from django.test import TestCase


class TestCommunity(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test_user', password='test_password')
        self.user.set_password('test_password')
        self.user.save()
        self.login = self.client.login(
            username='test_user', password='test_password')

    def test_communinity_create(self):
        """Test that users can create community"""
        self.assertTrue(self.login)
        response = self.client.post('/community/create', {
            'name': 'Test Community',
            'description': 'This is a test community',
            'private': True,
            'visibility': 'none',
            'default_group_permissions': ['BLOCK_MEMBER'],
            'creator': self.user
        })

        # Test redirection to single community view
        self.assertEqual(response.status_code, 302)

        # Test community is created
        self.assertTrue(Community.objects.exists())
        self.assertTrue(Community.objects.filter(
            name='Test Community', creator=self.user))

        # Test community creator is member
        self.assertTrue(CommunityMember.objects.exists())
        self.assertTrue(CommunityMember.objects.filter(
            user=self.user, community=Community.objects.get(name='Test Community')))

    def test_communinity_list(self):
        """Test that users can view list of communities"""
        self.assertTrue(self.login)

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
