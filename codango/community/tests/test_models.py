import factories
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from community.models import AddOn, Community, Tag


class AddonModelTestSuite(TestCase):
    def setUp(self):
        tags = factories.TagFactory.build_batch(2)
        addons = factories.AddOnFactory.build_batch(2)

        # self.tag1 = Tag.objects.create(title=tags[0])
        # self.tag2 = Tag.objects.create(title=tags[1])

        # self.user = User.objects.create(
        #     username=factories.UserFactory.username,
        #     password=factories.UserFactory.password
        # )

        # self.community1 = Community.objects.create(
        #     name=community[0].name,
        #     description=community[0].description,
        #     creator=self.user
        # )
        # self.community1.tags.add(self.tag1)
        # self.community1.save()
        # self.community2 = Community.objects.create(
        #     name=community[1].name,
        #     description=community[1].description,
        #     creator=self.user
        # )
        # self.community1.tags.add(self.tag2)

        self.community = factories.CommunityFactory.create()

        self.addon1 = AddOn.objects.create(name=addons[0].name)
        self.addon2 = AddOn.objects.create(name=addons[1].name)
        self.addon1.communities.add(self.community1)

    def test_can_create_addon(self):
        addon = AddOn.objects.create(name="pairprogram")
        self.assertIsInstance(addon, AddOn)
        self.assertIsNotNone(addon.id)
        self.assertIsNotNone(addon.name)

    def test_can_read_addon(self):
        addon = AddOn.objects.get(name=addons[0].name)
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
