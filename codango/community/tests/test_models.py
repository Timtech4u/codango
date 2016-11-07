import factories
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from community.models import AddOn, Community, Tag


class AddonModelTestSuite(TestCase):
    def setUp(self):
        self.addons = factories.AddOnFactory.build_batch(2)
        self.communities = factories.CommunityFactory.create()
        self.user = factories.UserFactory()

        self.addon = AddOn.objects.create(name=self.addons[0].name)

    def test_can_create_addon(self):
        addon = AddOn.objects.create(name="pairprogram")
        self.assertIsInstance(addon, AddOn)
        self.assertIsNotNone(addon.id)
        self.assertIsNotNone(addon.name)

    def test_can_read_addon(self):
        addon = AddOn.objects.get(name=self.addons[0].name)
        self.assertIsInstance(addon, AddOn)

    def test_can_update_addon(self):
        addon = AddOn.objects.get(name=self.addons[0].name)
        addon.name = "analytics"
        addon.save()
        addon = AddOn.objects.get(name="analytics")
        self.assertEqual(addon.id, self.addon.id)
        self.assertEqual(addon.name, "analytics")

    def test_can_delete_addon(self):
        addon = AddOn.objects.get(name=self.addons[0].name)
        addon.delete()
        self.assertRaises(
            ObjectDoesNotExist,
            AddOn.objects.get,
            pk=self.addon.id
        )

    def test_can_read_community_from_addon(self):
        self.addon.communities.add(self.communities)
        addon = AddOn.objects.get(name=self.addons[0].name)
        community = self.addon.communities.get(name=self.communities.name)
        self.assertIsInstance(community, Community)

    def test_can_add_community_to_addon(self):
        self.addon.communities.add(self.communities)
        community = self.addon.communities.get(name=self.communities.name)
        self.assertEqual(community, self.communities)

    def test_can_add_multiple_communities_to_addon(self):
        self.addon.communities.add(self.communities)
        self.community2 = factories.CommunityFactory.create(name='community2')
        self.addon.communities.add(self.community2)
        self.assertEqual(self.addon.communities.all().count(), 2)

    def test_can_remove_addon_from_community(self):
        self.addon.communities.add(self.communities)
        self.assertEqual(self.addon.communities.all().count(), 1)
        self.addon.communities.remove(self.communities)
        self.assertEqual(self.addon.communities.all().count(), 0)

    def test_add_invalid_object_to_addon(self):
        self.assertRaises(
            TypeError,
            self.addon.communities.add,
            self.user
        )
