import factory
import datetime
from community.tests.factories import UserFactory
from freezegun import freeze_time
from resources.tests.factories import ResourceFactory
from votes import models


@freeze_time("2016-09-14 12:00:01")
class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Vote

    user = factory.SubFactory(UserFactory)
    resource = factory.SubFactory(ResourceFactory)
    vote = False
    time_stamp = datetime.datetime.now()
