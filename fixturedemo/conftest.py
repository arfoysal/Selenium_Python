import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fixturedemo import settings


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome"
    parser.addoption("--browser", action="store", default=settings.browser)


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@pytest.fixture
def get_driver(request, get_browser):
    _driver = None
    if get_browser == "chrome":
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif get_browser == "firefox":
        _driver = webdriver.Firefox(executable_path="C:/browser_driver/geckodriver")
    _driver.implicitly_wait(15)
    _driver.set_page_load_timeout(15)
    _driver.get("https://www.saucedemo.com/index.html")
    _driver.maximize_window()
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()
