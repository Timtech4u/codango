import factory

from pairprogram import models


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Session


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Participant
