from selenium.webdriver.common.by import By

from POM_practice.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    products_text = (By.CSS_SELECTOR, "div[class='product_label']")
    inventoryItems = (By.CSS_SELECTOR, ".inventory_item")
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
    remove_first_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory")
    remove_second_item = (By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory")
    sort_selector = (By.CSS_SELECTOR, ".product_sort_container")
    first_item_name = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_name")
    first_item_price = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price")

    def wait_for_product_text(self):
        self.wait_for(self.products_text)

    def get_items_count(self):
        return self.get_count(self.inventoryItems)