import datetime
import factory
from community.tests.factories import CommunityFactory, UserFactory
from resources import models


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Resource

    author = factory.RelatedFactory(UserFactory)
    community = factory.RelatedFactory(CommunityFactory)
    text = 'This is a sample resource text'
    language_tags = 'PYTHON'
    date_added = factory.LazyAttribute(
        lambda o: o.datetime.now() - datetime.timedelta(hours=1))
    date_modified = datetime.now()


class NotificationQueueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NotificationQueue

    user = factory.RelatedFactory(UserFactory)
    notification_type = "Notification Type"
    first_interaction = "first interaction"
    count = 1
