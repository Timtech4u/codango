from datetime import datetime
import factory

from account import models


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContactModel

    name = factory.Sequence(lambda n: "New Person %d" % n)
    email = factory.LazyAttribute(
        lambda a: '{0}@domain.com'.format(
            a.name.replace(' ', '')).lower())
    subject = factory.Sequence(lambda n: "Subject %d" % n)
    message = factory.Sequence(lambda n: "My message %d" % n)
    date_sent = factory.LazyFunction(datetime.now)
