from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from community.models import AddOn, Community
from factories import AddOnFactory, CommunityFactory, UserFactory


class AddonModelTestSuite(TestCase):
    def setUp(self):
        self.addons = AddOnFactory.build()
        self.community = CommunityFactory()
        self.addon = AddOn.objects.create(name=self.addons.name)

    def test_can_create_addon(self):
        self.assertIsNotNone(self.addon.id)
        self.assertIsNotNone(self.addon.name)

    def test_can_read_addon(self):
        addon = AddOn.objects.get(name=self.addons.name)
        self.assertIsInstance(addon, AddOn)

    def test_can_update_addon(self):
        addon = AddOn.objects.get(name=self.addons.name)
        addon.name = "analytics"
        addon.save()
        addon = AddOn.objects.get(name="analytics")
        self.assertEqual(addon.id, self.addon.id)
        self.assertEqual(addon.name, "analytics")

    def test_can_delete_addon(self):
        addon = AddOn.objects.get(name=self.addons.name)
        addon.delete()
        self.assertRaises(
            ObjectDoesNotExist,
            AddOn.objects.get,
            pk=self.addon.id
        )

    def test_can_read_community_from_addon(self):
        self.addon.communities.add(self.community)
        addon = AddOn.objects.get(name=self.addons.name)
        community = addon.communities.get(name=self.community.name)
        self.assertIsInstance(community, Community)

    def test_can_add_community_to_addon(self):
        self.addon.communities.add(self.community)
        community = self.addon.communities.get(name=self.community.name)
        self.assertEqual(community, self.community)

    def test_can_add_multiple_communities_to_addon(self):
        self.addon.communities.add(self.community)
        self.community2 = CommunityFactory.create(name='community2')
        self.addon.communities.add(self.community2)
        self.assertEqual(self.addon.communities.all().count(), 2)

    def test_can_remove_addon_from_community(self):
        self.addon.communities.add(self.community)
        self.assertEqual(self.addon.communities.all().count(), 1)
        self.addon.communities.remove(self.community)
        self.assertEqual(self.addon.communities.all().count(), 0)

    def test_add_invalid_object_to_addon(self):
        self.assertRaises(
            TypeError,
            self.addon.communities.add,
            UserFactory()
        )
