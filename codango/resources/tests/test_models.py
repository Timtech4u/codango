from community.tests.factories import UserFactory
from django.contrib.auth.models import User
from django.test import TestCase
from factories import ResourceFactory
from mock import patch
from resources.models import Resource
from votes.models import Vote


class ResourceTestModels(TestCase):

    def setUp(self):
        user = UserFactory.build_batch(1)
        self.user = User.objects.create_user(
            username=user[0].username,
            password=user[0].password)
        self.resource = Resource.objects.create(
            text=ResourceFactory.text,
            author=self.user,
            resource_file=ResourceFactory.resource_file
        )

    def create_resources(
            self,
            text=ResourceFactory.text,
            resource_file=ResourceFactory.resource_file):
        return Resource.objects.create(
            text=text,
            author=self.user,
            resource_file=resource_file
        )

    def test_for_resource_creation(self):
        self.assertIsNotNone(Resource.objects.all())

    # mock cloudinary pre_save function that returns a public_id for uploads
    def test_file_save(self):
        with patch.object(
                Resource.resource_file.field,
                'pre_save', return_value='test.pdf') as mock_method:
            uploadlink = mock_method('test.pdf')
            self.resource.resource_file = uploadlink
            self.resource.save()
            resourcefile = Resource.objects.filter(
                resource_file=uploadlink)[0].resource_file
            publicid = resourcefile.public_id
            cloudinaryurl = resourcefile.url
            fileformat = resourcefile.format
            self.assertEqual(publicid, 'test')
            self.assertEqual(
                cloudinaryurl,
                'http://res.cloudinary.com/codangofile/image/upload/test.pdf')
            self.assertEquals(fileformat, 'pdf')
        create = self.create_resources()
        self.assertTrue(isinstance(create, Resource))

    def test_for_upvote(self):
        resource = self.create_resources()
        vote = Vote()
        vote.user = self.user
        vote.resource = resource
        vote.vote = True
        vote.save()
        self.assertEqual(len(resource.upvotes()), 1)

    def test_for_downvote(self):
        resource = self.create_resources()
        vote = Vote()
        vote.user = self.user
        vote.resource = resource
        vote.vote = False
        vote.save()
        self.assertEqual(len(resource.downvotes()), 1)
