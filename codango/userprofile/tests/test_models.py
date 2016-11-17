from django.test import TestCase
from userprofile.models import UserProfile, Language, Notification
from userprofile.tests.factories import (
    UserProfileFactory,
    LanguageFactory,
    NotificationFactory)


class ProfileTestModels(TestCase):

    def setUp(self):
        self.language = LanguageFactory()
        self.notification = NotificationFactory()

    def tearDown(self):
        UserProfile.objects.all().delete()
        Language.objects.all().delete()
        Notification.objects.all().delete()

    def test_for_profile_creation(self):
        self.user = UserProfileFactory()
        userprofile = UserProfile.objects.get(
            user=self.user.user)
        self.assertTrue(isinstance(userprofile, UserProfile))

    def test_for_language(self):
        language = str(self.language)
        self.assertIsNotNone(language)

    def test_for_notificaiotn(self):
        notification = str(self.notification)
        self.assertIsNotNone(notification)
