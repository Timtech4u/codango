import os
import cloudinary

from django.conf import settings
from django.test import TestCase

from community.models import Community, CommunityMember
from django.contrib.auth.models import User
from factories import CommunityFactory, CommunityMemberFactory, UserFactory


class TestCommunity(TestCase):

    def setUp(self):
        user = UserFactory.build()
        self.user = User.objects.create_user(
            username=user.username,
            password=user.password)
        self.login = self.client.login(
            username=user.username,
            password=user.password)
        self.assertTrue(self.login)
        self.community = CommunityFactory()
        self.community_member = CommunityMemberFactory()

    def test_community_create(self):
        """Test that users can create community"""
        image_abs_path = os.path.join(
            settings.BASE_DIR, 'static/img/sample.png')
        test_image_path = open(image_abs_path, 'rb')
        response = self.client.post(
            '/community/create',
            {'name': 'Test Community',
             'description': 'This is a test community',
             'logo': test_image_path,
             'private': True,
             'visibility': 'none',
             'default_group_permissions': ['BLOCK_MEMBER'],
             'creator': self.user
             })
        test_image_path.close()

        # Test redirection to single community view
        self.assertEqual(response.status_code, 302)

        # Test community is created
        self.assertTrue(Community.objects.exists())
        self.assertTrue(Community.objects.filter(
            name='Test Community',
            creator=self.user))

        # Test community creator is member
        self.assertTrue(CommunityMember.objects.exists())
        self.assertTrue(CommunityMember.objects.filter(
            user=self.user,
            community=Community.objects.get(name='Test Community')))

        # Test logo is being uploaded
        self.assertIn(
            'sample',
            Community.objects.filter(name='Test Community')[0].logo.public_id)

        # Delete the logo from Cloudinary's CDN
        cloudinary.uploader.destroy(str(Community.objects.filter(
            name='Test Community')[0].logo.public_id),
            invalidate=True)

    def test_public_community_is_listed(self):
        """Test that public community is listed"""

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])

    def test_fully_visible_private_community_is_listed(self):
        """Test that fully-visible private community is listed"""
        # Create a fully-visible private community
        self.community = CommunityFactory(private=True)

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])

    def test_partially_visible_private_community_is_listed(self):
        """Test that partially-visible private community is listed"""
        # Create a partially-visible private community
        self.community = CommunityFactory(private=True, visibility='partial')

        # Go to Community List Page
        response = self.client.get('/community/')

        # Test view community list
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.community, response.context_data['communities'])
