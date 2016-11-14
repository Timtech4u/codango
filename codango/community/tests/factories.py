import factory

from community import models
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "trial user %d" % n)
    email = factory.LazyAttribute(
        lambda a: '{0}@yahoo.com'.format(
            a.username.replace(' ', '')).lower())
    password = factory.LazyAttribute(
        lambda a: '{0}'.format(
            a.username.replace(' ', '')))


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    title = "Test_tag"


class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Community

    name = 'Test Community'
    description = 'This is a test community'
    private = False
    visibility = 'full'
    creator = factory.RelatedFactory(UserFactory)
    tags = factory.RelatedFactory(TagFactory)


class PermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Permission

    label = 'BLOCK_MEMBER'
    description = 'Block members'


class CommunityMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityMember

    community = factory.RelatedFactory(CommunityFactory)
    user = UserFactory
    invitor = factory.RelatedFactory(UserFactory)


class CommunityBlacklistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityBlacklist

    user = factory.RelatedFactory(UserFactory)
    blacklister = factory.RelatedFactory(CommunityMemberFactory)
    community = factory.RelatedFactory(CommunityFactory)


class AddOnFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AddOn

    name = 'test_addon'
    community = factory.SubFactory(CommunityFactory)
