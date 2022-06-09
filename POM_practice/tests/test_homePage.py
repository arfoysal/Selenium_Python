from POM_practice.tests import settings
from POM_practice.tests.base_test import BaseTest


class TestHome(BaseTest):
    def test_products(self):
        self.loginPage.login(settings.username, settings.password)
        self.homePage.wait_for()
