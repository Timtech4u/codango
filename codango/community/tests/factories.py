import factory

from community import models


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
    creator = 'User'
    tag = factory.RelatedFactory(TagFactory)


class PermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Permission

    label = 'BLOCK_MEMBER'
    description = 'Block members'


class CommunityMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityMember

    community = factory.RelatedFactory(CommunityFactory)
    user = '????'
    invitor = '????'
    status = 'pending'
    permission = factory.SubFactory(PermissionFactory)


class CommunityBlacklistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityBlacklist


class AddOnFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AddOn

    name = 'Test_Addon'
    community = factory.SubFactory(CommunityFactory)
