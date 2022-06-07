from selenium.webdriver.common.by import By

from POM_practice.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginButton = (By.ID, "login-button")

    def login(self, username, password):
        self.send_text(self.username, username)
        self.send_text(self.password, password)
        self.click_on(self.loginButton)
