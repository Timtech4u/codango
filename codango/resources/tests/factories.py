import factory
from community.tests.factories import CommunityFactory, UserFactory
from datetime import datetime, timedelta
from freezegun import freeze_time
from resources import models


@freeze_time("2016-09-14 12:00:01")
class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Resource

    author = factory.SubFactory(UserFactory)
    community = factory.SubFactory(CommunityFactory)
    text = 'This is a sample resource text'
    language_tags = 'PYTHON'
    date_added = datetime.now()
    date_modified = date_added + timedelta(hours=1)
    resource_file = 'resource_file'


class NotificationQueueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NotificationQueue

    user = factory.SubFactory(UserFactory)
    notification_type = "Notification Type"
    first_interaction = "first interaction"
    count = 1
