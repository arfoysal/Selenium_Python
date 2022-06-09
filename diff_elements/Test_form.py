import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def validet_str(text):
    text_list = text.split(":")
    return text_list[1]


class TestQAForm:

    def test_form(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(35)
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()

        assert "ToolsQA" == driver.title
        first_name = "DEMOUSERNAME"
        email = "test@email.com"
        current_address = "Our Address"
        permanent_address = "Our Permanent Address value"

        driver.find_element(By.ID, "userName").send_keys(first_name)
        driver.find_element(By.ID, "userEmail").send_keys(email)
        driver.find_element(By.ID, "currentAddress").send_keys(current_address)
        driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)
        driver.find_element(By.XPATH, "//button[@id='submit']").click()

        assert first_name == validet_str(driver.find_element(By.ID, "name").text)
        assert email == validet_str(driver.find_element(By.ID, "email").text)
        assert current_address == validet_str(driver.find_element(By.ID, "currentAddress").text)
        assert permanent_address == validet_str(driver.find_element(By.ID, "permanentAddress").text)

        driver.quit()
