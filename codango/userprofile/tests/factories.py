import factory

from account import models


class ContactModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContactModel
