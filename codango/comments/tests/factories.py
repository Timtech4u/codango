import factory

from comments import models
from community.tests.factories import UserFactory
from datetime import datetime
from resource.tests.factories import ResourceFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment

    author = factory.RelatedFactory(UserFactory)
    resource = factory.RelatedFactory(ResourceFactory)
    content = 'This is a sample comment'
    date_created = factory.LazyAttribute(
        lambda o: o.datetime.now() - datetime.timedelta(hours=1))
    date_modified = datetime.now()
