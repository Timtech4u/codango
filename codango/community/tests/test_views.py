import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.utils import setup_test_environment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

setup_test_environment()


class TestCommuntity(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def create_new_community(self, private=False, visibility='Full'):
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

        # Create the community
        name_field = self.browser.find_element_by_name(
            'name')
        name_field.send_keys('A New community')
        description_field = self.browser.find_element_by_name(
            'description')
        description_field.send_keys('This is a new community')
        private_field = self.browser.find_element_by_name(
            'private')
        private_field.send_keys(private)
        visibility_field = self.browser.find_element_by_name(
            'visibility')
        self.browser.execute_script(
            'arguments[0].removeAttribute("disabled");', visibility_field)
        visibility_field.send_keys(visibility)
        default_group_permissions_field = self.browser.find_element_by_name(
            'default_group_permissions')
        default_group_permissions_field.send_keys('Send invites')
        self.browser.find_element_by_id('community_submit').click()

    def test_can_create_community(self):
        # Create a new community
        self.create_new_community()

        # Assert community is created
        body = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Create A New Community', body.text)

    def test_can_view_community_list(self):
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

        # View List Communities page
        list_community_buttons = self.browser.find_elements_by_class_name(
            'list-community')
        for button in list_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango Communities', body.text)

    def test_public_community_is_listed(self):

        # Create a new public community
        self.create_new_community()

        # View List Communities page
        list_community_buttons = self.browser.find_elements_by_class_name(
            'list-community')
        for button in list_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')

        # Assert Created community is listed
        self.assertIn('Codango Communities', body.text)
        self.assertIn('A New community', body.text)
        self.assertIn('This is a new community', body.text)

    def test_fully_visible_private_community_is_listed(self):

        # Create a fully visible private community
        self.create_new_community(private=True, visibility='Full')

        # View List Communities page
        list_community_buttons = self.browser.find_elements_by_class_name(
            'list-community')
        for button in list_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')

        # Assert Created community is listed
        self.assertIn('Codango Communities', body.text)
        self.assertIn('A New community', body.text)
        self.assertIn('This is a new community', body.text)

    def test_partially_visible_private_community_is_listed(self):

        # Create a partially-visible private community
        self.create_new_community(private=True, visibility='Partial')

        # View List Communities page
        list_community_buttons = self.browser.find_elements_by_class_name(
            'list-community')
        for button in list_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')

        # Assert Created community is listed
        self.assertIn('Codango Communities', body.text)
        self.assertIn('A New community', body.text)
        self.assertIn('This is a new community', body.text)

    def test_non_visible_private_community_is_not_listed(self):

        # Create a non-visible private community
        self.create_new_community(private=True, visibility='None')

        # View List Communities page
        list_community_buttons = self.browser.find_elements_by_class_name(
            'list-community')
        for button in list_community_buttons:
            if button.is_displayed():
                button.click()
                break
        body = self.browser.find_element_by_tag_name('body')

        # Assert Created community is not listed
        self.assertIn('Codango Communities', body.text)
        self.assertNotIn('A New community', body.text)
        self.assertNotIn('This is a new community', body.text)
