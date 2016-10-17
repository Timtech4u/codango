from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from ..models import Community, Tag, AddOn


class AddonModelTestSuite(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="regularjoe",
            email="regularjoe@yahoo.com",
            password="regularjoepass"
        )

        tag = Tag.objects.create(title="Python")
        self.community_python = Community.objects.create(
            name="pythonistas",
            description="A chill place for python lovers",
            creator=self.user
        )
        self.community_python.tags.add(tag)
        self.community_ruby = Community.objects.create(
            name="Ruby Tabernacle",
            description="We eat gems and talk ruby",
            creator=self.user
        )
        self.community_ruby.tags.add(tag)

        self.addon_statistics = AddOn.objects.create(name="statistics")
        self.addon_bots = AddOn.objects.create(name="bots")
        self.addon_statistics.communities.add(self.community_python)

    def test_can_create_addon(self):
        addon = AddOn.objects.create(name="pairprogram")
        self.assertIsInstance(addon, AddOn)
        self.assertIsNotNone(addon.id)
        self.assertIsNotNone(addon.name)

    def test_can_read_addon(self):
        addon = AddOn.objects.get(name="statistics")
        self.assertIsInstance(addon, AddOn)

    def test_can_update_addon(self):
        addon = AddOn.objects.get(name="statistics")
        addon.name = "analytics"
        addon.save()
        addon = AddOn.objects.get(name="analytics")
        self.assertEqual(addon.id, self.addon_statistics.id)
        self.assertEqual(addon.name, "analytics")

    def test_can_delete_addon(self):
        addon = AddOn.objects.get(name="statistics")
        addon.delete()
        self.assertRaises(
            ObjectDoesNotExist,
            AddOn.objects.get,
            pk=self.addon_statistics.id
        )

    def test_can_read_community_from_addon(self):
        addon = AddOn.objects.get(name="statistics")
        community = addon.communities.get(name="pythonistas")
        self.assertIsInstance(community, Community)

    def test_can_add_community_to_addon(self):
        self.addon_bots.communities.add(self.community_ruby)
        community = self.addon_bots.communities.get(name="Ruby Tabernacle")
        self.assertEqual(community, self.community_ruby)

    def test_can_add_multiple_communities_to_addon(self):
        self.addon_statistics.communities.add(self.community_ruby)
        self.assertEqual(self.addon_statistics.communities.all().count(), 2)

    def test_can_remove_addon_from_community(self):
        self.addon_statistics.communities.remove(self.community_python)
        self.assertEqual(self.addon_statistics.communities.all().count(), 0)

    def test_add_invalid_object_to_addon(self):
        self.assertRaises(
            TypeError,
            self.addon_statistics.communities.add,
            self.user
        )
