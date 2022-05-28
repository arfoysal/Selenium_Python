import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Test_WebPageLoad:
    driver = None

    def test_google_page_load(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(60)
        driver.get("https://www.google.com/")
        assert "Google" in driver.title
        driver.save_screenshot("./images/test.png")
        time.sleep(5)
        driver.quit()

    def test_facebook_page_load(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(60)
        driver.get("https://www.facebook.com/")
        assert "Google" in driver.title
        driver.save_screenshot("./images/test1.png")
        time.sleep(5)
        driver.quit()
