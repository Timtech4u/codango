import factory

from userprofile import models


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserProfile


class UserSettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserSettings


class FollowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Follow


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Language


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Notification
