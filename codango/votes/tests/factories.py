import factory

from resources import models


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Vote
