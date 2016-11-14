from community.tests.factories import UserFactory
from django.contrib.auth.models import User
from django.test import TestCase
from factories import VoteFactory
from resources.models import Resource
from resources.tests.factories import ResourceFactory
from votes.models import Vote


class VoteTestModels(TestCase):

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

    def test_for_vote_creation(self):
        resource = self.create_resources()
        vote = Vote.objects.create(
            resource=resource,
            user=self.user,
            vote=VoteFactory.vote)
        self.assertTrue(isinstance(vote, Vote))

    def test_for_vote_is_down_vote(self):
        resource = self.create_resources()
        vote = Vote.objects.create(
            resource=resource,
            user=self.user,
            vote=VoteFactory.vote)

        self.assertTrue(vote.is_downvote())

    def test_for_vote_is_up_vote(self):
        resource = self.create_resources()
        vote = Vote.objects.create(
            resource=resource,
            user=self.user,
            vote=True)

        self.assertTrue(vote.is_upvote())
