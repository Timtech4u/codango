from comments.models import Comment
from community.tests.factories import UserFactory
from django.contrib.auth.models import User
from django.test import TestCase
from factories import CommentFactory
from resources.models import Resource
from resources.tests.factories import ResourceFactory


class CommentTestModels(TestCase):

    def setUp(self):
        user = UserFactory.build_batch(1)
        self.user = User.objects.create_user(
            username=user[0].username,
            password=user[0].password)

    def create_resources(
            self,
            text=ResourceFactory.text,
            resource_file=ResourceFactory.resource_file):
        return Resource.objects.create(
            text=text,
            author=self.user,
            resource_file=resource_file
        )

    def test_for_comment_creation(self):
        resource = self.create_resources()
        comment = Comment.objects.create(
            resource=resource,
            author=self.user,
            content=CommentFactory.content
        )
        self.assertTrue(isinstance(comment, Comment))

    def test_for_comment_str_content(self):
        resource = self.create_resources()
        comment = Comment.objects.create(
            resource=resource,
            author=self.user,
            content=CommentFactory.content
        )
        content = str(comment)
        self.assertIsNotNone(content)
