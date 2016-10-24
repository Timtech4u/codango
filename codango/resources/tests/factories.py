import factory

from resources import models


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Resource


class NotificationQueueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NotificationQueue
