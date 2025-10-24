from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LoginPage(BasePage):
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    ERROR_MESSAGE = (By.CLASS_NAME, "woocommerce-error")
    DASHBOARD_LINK = (By.LINK_TEXT, "Dashboard")
    
    def login(self, username, password):
        self.enter_text(self.LOGIN_USERNAME, username)
        self.enter_text(self.LOGIN_PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(3)
    
    def is_logged_in(self):
        return (self.is_element_visible(self.LOGOUT_LINK) or 
                self.is_element_visible(self.DASHBOARD_LINK))
    
    def get_error_message(self):
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""