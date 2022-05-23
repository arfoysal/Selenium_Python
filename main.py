import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(60)
driver.get("https://www.google.com/")
driver.save_screenshot("./test.png")
time.sleep(5)