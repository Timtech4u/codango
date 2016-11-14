from django.test import TestCase

from comments.models import Comment
from factories import CommentFactory
from resources.tests.factories import ResourceFactory


class CommentTestModels(TestCase):

    def setUp(self):
        self.resource = ResourceFactory()
        self.comment = CommentFactory()

    def test_for_comment_creation(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_for_comment_str_content(self):
        content = str(self.comment)
        self.assertIsNotNone(content)
