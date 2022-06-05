import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_drop_down():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.get("https://qavbox.github.io/demo")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "SignUp Form").click()

    select = Select(driver.find_element(By.NAME, "sgender"))
    select.select_by_value("male")

    print("Selected option  " + select.first_selected_option.text)
    options = select.options
    print("the available options are ")
    for option in options:
        print(option.text)

    time.sleep(3)
    driver.quit()