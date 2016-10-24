import factory

from community import models


class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Community


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    title = "Test_tag"


class PermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Permission


class CommunityMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityMember


class CommunityBlacklistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CommunityBlacklist


class AddOnFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AddOn

    community = factory.SubFactory(CommunityFactory)
