from POM_practice.tests import settings
from POM_practice.tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        self.loginPage.login(settings.username, settings.password)
        self.homepage.wait_for_product_text()

    def test_locked_user_login(self):
        self.loginPage.login(settings.locked_username, settings.password)
        assert "Epic sadface: Sorry, this user has been locked out" in self.loginPage.get_locked_error_text()


