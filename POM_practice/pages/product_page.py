from selenium.webdriver.common.by import By

from POM_practice.pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_text = (By.CSS_SELECTOR, "div[class='product_label']")

    def wait_for_product_text(self):
        self.wait_for(self.product_text)

