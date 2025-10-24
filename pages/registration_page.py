from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class RegistrationPage(BasePage):
    REG_EMAIL = (By.ID, "reg_email")
    REG_PASSWORD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.NAME, "register")
    ERROR_MESSAGE = (By.CLASS_NAME, "woocommerce-error")
    
    def register_new_user(self, email, password):
        self.enter_text(self.REG_EMAIL, email)
        self.enter_text(self.REG_PASSWORD, password)
        self.click_element(self.REGISTER_BUTTON)
        time.sleep(3)
    
    def get_error_message(self):
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""