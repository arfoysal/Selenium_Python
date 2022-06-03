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


class Test_iframe_text(BaseTest):
    def test_text(self):
        self.driver.get("https://demoqa.com/frames")
        assert self.driver.title == "ToolsQA"
        self.driver.switch_to.frame(self.driver.find_element_by_id("frame1"))
        assert self.driver.find_element_by_id("sampleHeading").text == "This is a sample page"
        self.driver.switch_to.default_content()



