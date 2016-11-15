import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import Client, TestCase
from django.test.utils import setup_test_environment

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from community.models import AddOn, Community
from django.contrib.auth.models import User
from factories import AddOnFactory, CommunityFactory
from factories import CommunityMemberFactory, UserFactory


setup_test_environment()


class TestCreateCommuntity(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_community(self):
        self.browser.get(self.live_server_url)

        # logging in username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)
        time.sleep(10)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Share', body.text)

        # View Create Community page
        create_community_buttons = self.browser.find_elements_by_id(
            'create-community')
        for button in create_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Create A New Community', body.text)

        # Create a new community
        name_field = self.browser.find_element_by_name(
            'name')
        name_field.send_keys('A New community')
        description_field = self.browser.find_element_by_name(
            'description')
        description_field.send_keys('This is a new community')
        private_field = self.browser.find_element_by_name(
            'private')
        private_field.send_keys(True)
        visibility_field = self.browser.find_element_by_name(
            'visibility')
        self.browser.execute_script(
            'arguments[0].removeAttribute("disabled");', visibility_field)
        visibility_field.send_keys('None')
        default_group_permissions_field = self.browser.find_element_by_name(
            'default_group_permissions')
        default_group_permissions_field.send_keys('Send invites')
        self.browser.find_element_by_id('community_submit').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Create A New Community', body.text)


class JoinCommunityTest(TestCase):

    def setUp(self):
        users = UserFactory.build_batch(2)
        user1 = users[0]
        user2 = users[1]
        self.user = User.objects.create_user(
            username=user1.username,
            password=user1.password)
        self.login = self.client.login(
            username=user1.username,
            password=user1.password)
        self.assertTrue(self.login)
        self.public_community = CommunityFactory(name='public_community')
        self.private_community = CommunityFactory(name='private_community')
        self.user_to_join_community = User.objects.create_user(
            username=user2.username,
            password=user2.password)
        self.login = self.client.login(
            username=user2.username,
            password=user2.password)
        self.community = CommunityMemberFactory(
            community=self.public_community,
            status="approved")

    def test_user_can_join_public_community(self):
        """Test user can join a public community"""
        self.assertTrue(self.login)
        data = {'community': self.public_community,
                'user': self.user_to_join_community,
                'invitor': self.user, 'status': 'approved'}
        self.assertEqual(self.public_community.get_no_of_members(), 1)
        url = "/community/{}".format(self.public_community.id)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_cant_join_private_community(self):
        """Test user cannot join a private community"""
        data = {'community': self.private_community,
                'user': self.user_to_join_community,
                'invitor': self.user, 'status': 'approved'}
        self.assertTrue(self.login)
        self.assertTrue(self.private_community.get_no_of_members() == 0)
        url = "/community/{}".format(self.private_community.id)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_user_cant_join_public_community_twice(self):
        """Test user can join a public community twice"""
        self.assertTrue(self.login)
        self.assertEqual(self.public_community.get_no_of_members(), 1)
        try:
            community = CommunityMemberFactory(
                community=self.public_community,
                user=self.user_to_join_community,
                invitor=self.user,
                status="approved")
            community.save()
        except IntegrityError as e:
            self.assertIn("columns community_id, user_id are not unique",
                          e.message)


class AddOnListViewTest(TestCase):
    def setUp(self):
        user = UserFactory.build()
        self.user = User.objects.create_user(
            username=user.username,
            password=user.password)
        self.community = Community.objects.create(
            name=CommunityFactory.name,
            description=CommunityFactory.description,
            private=CommunityFactory.private,
            visibility=CommunityFactory.visibility,
            creator=self.user)
        addon = AddOnFactory.build()
        self.addon = AddOn.objects.create(name=addon.name)
        self.client = Client()
        self.client.login(
            username=user.username,
            password=user.password)

    def test_user_can_retrieve_addon_list(self):
        url = reverse('addon_list',
                      kwargs={'community_id': self.community.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.addon.name, response.content)

    def test_creator_can_link_addon(self):
        data = {'addons_check': [self.addon.name]}
        url = reverse('addon_list',
                      kwargs={'community_id': self.community.id})
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        community_addon = self.community.addon_set.get(
            name=self.addon.name)
        self.assertEqual(community_addon.name, self.addon.name)

    def test_member_cant_link_addon(self):
        self.user = User.objects.create_user(
            username='Member',
            password='member')
        self.client.login(username='Member', password='member')
        url = reverse('addon_list',
                      kwargs={'community_id': self.community.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
