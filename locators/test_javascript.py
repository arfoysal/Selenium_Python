import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_javascript():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.get("https://qavbox.github.io/demo/webtable/")
    driver.maximize_window()
    assert "webtable" in driver.title


    driver.execute_script("window.location = 'https://qavbox.github.io/demo/'")
    print("Title : " + driver.execute_script("return document.title"))
    print("url : " + driver.execute_script("return document.URL"))
    print("is page loaded - " + driver.execute_script("return document.readyState"))
    time.sleep(5)
    element = driver.execute_script("return document.querySelector(\"[href='/demo/signup']\")")
    driver.execute_script("arguments[0].click();", element)

    driver.execute_script("return document.getElementById('username').value='Foysal'")
    print("Entered value - " + driver.execute_script("return document.getElementById('username').value"))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.execute_script("document.querySelector(\"input[value='seven']\").checked=true")
    time.sleep(5)
    driver.quit()
