import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(params=["chrome"] ,scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"

