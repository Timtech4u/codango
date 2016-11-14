import factory
from community.tests.factories import UserFactory
from django.utils import timezone
from userprofile import models


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserProfile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    social_id = factory.Sequence(
        lambda n: int("{}".format(n)))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    place_of_work = factory.Faker('company')
    position = factory.Faker('job')
    about = factory.LazyAttribute(
        lambda a: 'About {} {}'.format(
            a.first_name, a.last_name))
    github_username = factory.LazyAttribute(
        lambda a: '{}-{}'.format(
            a.first_name, a.last_name))
    frequency = 'none'
    like_preference = False
    comment_preference = False
    last_action = factory.LazyFunction(timezone.now)


class UserSettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserSettings

    user = factory.SubFactory(UserFactory)
    frequency = "daily"


class FollowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Follow

    follower = factory.SubFactory(UserFactory)
    followed = factory.SubFactory(UserFactory)
    date_of_follow = factory.LazyFunction(timezone.now)


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Language

    user = factory.SubFactory(UserFactory)
    name = factory.Sequence(
        lambda n: "Language {}".format(n))


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Notification

    user = factory.SubFactory(UserFactory)
    link = factory.Sequence(
        lambda n: "Link {}".format(n))
    activity_type = factory.Sequence(
        lambda n: "Activity {}".format(n))
    read = False
    content = factory.Sequence(
        lambda n: "Notification content {}".format(n))
    date_created = factory.LazyFunction(timezone.now)
