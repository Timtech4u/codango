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
        self.assertTrue(self.login)

    def create_community(self, private=False, visibility='full'):
        self.community = Community.objects.create(name='Test Community',
                                                  description='This is a test community',
                                                  private=private,
                                                  visibility=visibility,
                                                  creator=self.user)

    def test_community_create(self):
        """Test that users can create community"""
        response = self.client.post('/community/create',
                                    {'name': 'Test Community',
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
        self.assertTrue(Community.objects.filter(name='Test Community',
                                                 creator=self.user))

        # Test community creator is member
        self.assertTrue(CommunityMember.objects.exists())
        self.assertTrue(CommunityMember.objects.filter(user=self.user,
                                                       community=Community.objects.get(name='Test Community')))

    def test_public_community_is_listed(self):
        """Test that public community is listed"""
        # Create a public community
        self.create_community()

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])

    def test_fully_visible_private_community_is_listed(self):
        """Test that fully-visible private community is listed"""
        # Create a fully-visible private community
        self.create_community(private=True, visibility='full')

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])

    def test_partially_visible_private_community_is_listed(self):
        """Test that partially-visible private community is listed"""
        # Create a partially-visible private community
        self.create_community(private=True, visibility='partial')

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])
