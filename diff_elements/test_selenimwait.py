import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def test_diff_wait():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.get("https://qavbox.github.io/demo/delay/")
    driver.maximize_window()
    assert "Delay" in driver.title

    commit_btn = driver.find_element(By.NAME, "commit")
    commit_btn.click()

    el_text = driver.find_element(By.ID, "two")
    print("First attempt - " + el_text.text)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(By.ID, ))
    commit_btn = driver.find_element(By.NAME, "commit1")
    commit_btn.click()
    delay_element = driver.find_element(By.ID, "delay")
    print(delay_element.text)

    time.sleep(3)
    driver.quit()
