from django.test import TestCase

from community.tests.factories import UserFactory
from factories import VoteFactory
from votes.models import Vote


class VoteTestModels(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_for_vote_creation(self):
        vote = VoteFactory()
        self.assertTrue(isinstance(vote, Vote))

    def test_for_vote_is_down_vote(self):
        vote = VoteFactory()
        self.assertTrue(vote.is_downvote())

    def test_for_vote_is_up_vote(self):
        vote = VoteFactory(vote=True)
        self.assertTrue(vote.is_upvote())
