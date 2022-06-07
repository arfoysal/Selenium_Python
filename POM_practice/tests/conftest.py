import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from POM_practice.pages.base_page import BasePage
from POM_practice.pages.login_page import LoginPage
from POM_practice.pages.product_page import ProductPage
from POM_practice.tests import settings
driver = None

def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome"
    parser.addoption("--browser", action="store", default=settings.browser)


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif get_browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:/browser_driver/geckodriver")
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    driver.get(settings.url)
    driver.maximize_window()
    # request.cls.driver = driver
    # request.cls.BasePage = BasePage(driver)
    request.cls.loginPage = LoginPage(driver)
    request.cls.productPage = ProductPage(driver)

    #yield request.cls.driver
    yield driver
    time.sleep(2)
    #request.cls.driver.quit()
    driver.quit()
