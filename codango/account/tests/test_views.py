from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class IndexViewTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(30)
        self.browser.set_page_load_timeout(30)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_index_page_and_log_in_and_logout(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Collaborate', body.text)

        # open login modal
        self.browser.find_element_by_css_selector('button[role="login"]') \
            .click()

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

        # logging out
        self.browser.find_element_by_link_text('lade').click()
        self.browser.find_element_by_link_text('LogOut').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Collaborate', body.text)


class StaticPages(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_static_pages(self):
        self.browser.get(self.live_server_url)

        # index page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Collaborate', body.text)

        # about us page
        self.browser.find_element_by_link_text('Features').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Community', body.text)

        # contact us page
        self.browser.find_element_by_link_text('Contact Us').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Get In Touch', body.text)

        # team page
        self.browser.find_element_by_link_text('Team').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Team Members', body.text)
        self.assertIn('Hall Of Fame', body.text)
