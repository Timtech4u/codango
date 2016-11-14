from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.models import UserProfile, Language, Notification
from userprofile.tests.factories import \
    UserProfileFactory, LanguageFactory, NotificationFactory


class ProfileTestModels(TestCase):

    def setUp(self):
        self.user_factory = UserProfileFactory()
        self.language_factory = LanguageFactory(
            user=self.user_factory.user)
        self.notification_factory = NotificationFactory(
            user=self.user_factory.user)
        """self.user = User.objects.create(
                                    username='adebola', password='adebolu')
                                self.language = Language.objects.create(name="Python", user=self.user)
                                self.notification = Notification.objects.create(content="Python",
                                                                                user=self.user, read=False, link="link",
                                                                                activity_type="Vote")"""

    def test_for_profile_creation(self):
        userprofile = UserProfile.objects.get(
            first_name=self.user_factory.first_name)
        self.assertTrue(isinstance(userprofile, UserProfile))

    def test_for_language(self):
        language = str(self.language)
        self.assertIsNotNone(language)

    def test_for_notificaiotn(self):
        notification = str(self.notification)
        self.assertIsNotNone(notification)
