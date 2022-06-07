import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from fixturedemo.base_test import BaseTest


# @pytest.mark.usefixtures("get_driver")
class TestSauceDemoCount(BaseTest):
    def test_item_count(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label")))
        item_count = len(driver.find_elements(By.CSS_SELECTOR, "div[class='inventory_item']"))
        assert 6 == item_count
