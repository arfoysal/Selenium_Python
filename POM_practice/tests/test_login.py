from POM_practice.tests import settings
from POM_practice.tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        self.loginPage.login(settings.username, settings.password)
        self.productPage.wait_for_product_text()

