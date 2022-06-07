import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestDragDrop:

    def test_sample1(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.implicitly_wait(20)
        driver.set_page_load_timeout(30)
        driver.get("https://qavbox.github.io/demo/dragndrop/")
        driver.maximize_window()
        assert "DragnDrop" in driver.title

        action = ActionChains(driver)
        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")
        # action.drag_and_drop(source, target).perform()
        # action.click_and_hold(source).pause(2).move_to_element(target).perform()
        # action.click_and_hold(source).pause(2).move_to_element_with_offset(target, 100, 100).perform()
        action.drag_and_drop_by_offset(source, 170, 10).perform()
        print(target.text)
        assert "Dropped!" in target.text
        time.sleep(5)
        driver.quit()
