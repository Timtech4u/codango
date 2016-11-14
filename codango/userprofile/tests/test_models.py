from django.test import TestCase
from userprofile.models import UserProfile, Language, Notification
from userprofile.tests.factories import \
    UserProfileFactory, LanguageFactory, NotificationFactory


class ProfileTestModels(TestCase):

    def setUp(self):
        self.language_factory = LanguageFactory()
        self.notification_factory = NotificationFactory()

    def tearDown(self):
        UserProfile.objects.all().delete()
        Language.objects.all().delete()
        Notification.objects.all().delete()

    def test_for_profile_creation(self):
        self.user_factory = UserProfileFactory()
        userprofile = UserProfile.objects.get(
            user=self.user_factory.user)
        self.assertTrue(isinstance(userprofile, UserProfile))

    def test_for_language(self):
        language = str(self.language_factory)
        self.assertIsNotNone(language)

    def test_for_notificaiotn(self):
        notification = str(self.notification_factory)
        self.assertIsNotNone(notification)
