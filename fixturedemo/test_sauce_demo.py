import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

from fixturedemo.base_test import BaseTest


# @pytest.mark.usefixtures("get_driver")
class TestSauceDemo(BaseTest):

    def test_sauce_demo(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[class='product_label")))

