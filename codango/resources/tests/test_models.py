from django.test import TestCase
from mock import patch

from community.tests.factories import UserFactory
from factories import ResourceFactory
from resources.models import Resource
from votes.tests.factories import VoteFactory


class ResourceTestModels(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.resource = ResourceFactory()

    def test_for_resource_creation(self):
        self.assertIsNotNone(self.resource)

    # mock cloudinary pre_save function that returns a public_id for uploads
    def test_file_save(self):
        with patch.object(
                Resource.resource_file.field,
                'pre_save', return_value='test.pdf') as mock_method:
            uploadlink = mock_method('test.pdf')
            self.resource.resource_file = uploadlink
            self.resource.save()
            resourcefile = self.resource.resource_file
            publicid = resourcefile.public_id
            cloudinaryurl = resourcefile.url
            fileformat = resourcefile.format
            self.assertEqual(publicid, 'test')
            self.assertEqual(
                cloudinaryurl,
                'http://res.cloudinary.com/codangofile/image/upload/test.pdf')
            self.assertEquals(fileformat, 'pdf')
        self.assertTrue(isinstance(self.resource, Resource))

    def test_for_upvote(self):
        vote = VoteFactory()
        vote.user = self.user
        vote.resource = self.resource
        vote.vote = True
        vote.save()
        self.assertEqual(len(self.resource.upvotes()), 1)

    def test_for_downvote(self):
        vote = VoteFactory()
        vote.user = self.user
        vote.resource = self.resource
        vote.vote = False
        vote.save()
        self.assertEqual(len(self.resource.downvotes()), 1)
