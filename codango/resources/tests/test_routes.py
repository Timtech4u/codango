from community.models import Community
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.test.utils import setup_test_environment
from resources.models import Resource

setup_test_environment()


class CommunityViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='Abiodun', password='shuaib')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='Abiodun', password='shuaib')

    def create_resources(self, text='some more words',
                         resource_file='resource_file', community=None):
        return Resource.objects.create(id=100, text=text, author=self.user,
                                       resource_file=resource_file, community=community)

    def create_community(self, id):
        return Community.objects.create(id=id, name='Test Community',
                                        creator=self.user,
                                        description='This is a test community')

    def test_can_post_resource_to_community(self):
        # Create community
        community = self.create_community(id=100)

        # Post resource in a community
        response = self.client.post(reverse('resource_create', kwargs={'community_id': 100}),
                                    {'text': 'Sample post', },
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Resource.objects.filter(
            text='Sample post', community=community))

    def test_created_resource_belongs_to_community(self):
        # Create communities
        community = self.create_community(id=100)
        community2 = self.create_community(id=200)

        # Create a resource in community
        resource = self.create_resources(community=community)

        # Test for created resource
        self.assertIn(resource, community.resources.all())
        self.assertNotIn(resource, community2.resources.all())

    def test_created_resource_is_returned_in_context_data(self):
        # Create community
        community = self.create_community(id=100)

        # Create a resource in community
        resource = self.create_resources(community=community)

        # View community
        response = self.client.get(reverse('community_detail', kwargs={'community_id': 100}),
                                   content_type='application/json',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Test for created resource
        self.assertEqual(response.status_code, 200)
        self.assertIn(resource, response.context_data['resources'])

    def test_can_reach_ajax_community_page(self):
        self.assertTrue(self.login)
        response = self.client.get(
            reverse('community', args=('all',)),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(response.status_code == 200)
        self.assertContains(response, "There are currently no posts")

    def test_can_post_new_ajax_content(self):
        self.assertTrue(self.login)
        response = self.client.post(
            '/resource/create',
            {'text': '1', },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "status")

    def test_add_an_empty_resource(self):
        self.assertTrue(self.login)
        response = self.client.post(
            '/resource/newresource',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 404)

    def test_user_can_upvote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post(
            '/resource/100/likes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 1)

    def test_user_can_downvote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post(
            '/resource/100/unlikes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.downvotes()), 1)

    def test_user_can_get_persisten_vote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post(
            '/resource/100/unlikes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.post(
            '/resource/100/likes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 1)

    def test_user_cannot_vote_more_than_once(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post(
            '/resource/100/unlikes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.post(
            '/resource/100/unlikes', {'resource_id': 100},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 0)

    def test_user_can_view_single_resource(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.get('/resource/post/100')
        self.assertTrue(response.status_code, 200)

    def test_user_cannot_view_resource_that_does_not_exist(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.get('/resource/post/2')
        self.assertTrue(response.status_code, 404)
