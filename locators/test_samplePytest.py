import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSampleSel1:
    driver = None

    def test_sample_navigation(self):
        # TestSampleSel1.driver = webdriver.Chrome("C:/browser_driver/chromedriver")
        TestSampleSel1.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        TestSampleSel1.driver.implicitly_wait(20)
        TestSampleSel1.driver.set_page_load_timeout(30)
        TestSampleSel1.driver.get("https://qavbox.github.io/demo")
        assert "QAVBOX" in TestSampleSel1.driver.title

    def test_nav_reg(self):
        # driver.find_element_by_link_text("SignUp Form").click()
        TestSampleSel1.driver.find_element(By.LINK_TEXT, "SignUp Form").click()
        TestSampleSel1.driver.save_screenshot('./screenshot/signup.png')
        time.sleep(5)
        TestSampleSel1.driver.quit()
