from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class HomePage(BasePage):  
    SHOP_MENU = (By.LINK_TEXT, "Shop")
    MY_ACCOUNT_MENU = (By.LINK_TEXT, "My Account")
    CART_MENU = (By.CLASS_NAME, "cart-contents")
    HOME_MENU = (By.LINK_TEXT, "Home")
    
    def navigate_to_shop(self):
        self.click_element(self.SHOP_MENU)
        time.sleep(2)
    
    def navigate_to_my_account(self):
        self.click_element(self.MY_ACCOUNT_MENU)
        time.sleep(2)
    
    def navigate_to_cart(self):
        self.click_element(self.CART_MENU)
        time.sleep(2)