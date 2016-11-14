from django.utils import timezone
import factory

from community.tests.factories import UserFactory
from pairprogram import models


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Session

    session_name = factory.Sequence(lambda n: "Session %d" % n)
    language = factory.Sequence(lambda n: "Language %d" % n)
    last_active_date = factory.LazyFunction(timezone.now)
    status = True
    initiator = factory.SubFactory(UserFactory)


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Participant

    participant = factory.SubFactory(UserFactory)
    session = factory.SubFactory(SessionFactory)
    joined_date = factory.LazyFunction(timezone.now)
