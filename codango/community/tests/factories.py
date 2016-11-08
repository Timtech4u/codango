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

    title = factory.Sequence(lambda n: "Test_tag %d" % n)


class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Community

    name = factory.Sequence(lambda n: "Test_community %d" % n)
    description = 'This is a test community'
    private = False
    visibility = 'full'
    creator = factory.SubFactory(UserFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if extracted:
            for tag in extracted:
                self.tags.add(tag)


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

    name = factory.Sequence(lambda n: "Test_addon %d" % n)

    @factory.post_generation
    def communities(self, create, extracted, **kwargs):
        if extracted:
            for community in extracted:
                self.communities.add(community)
