from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ShopPage(BasePage):
    FIRST_PRODUCT = (By.XPATH, "(//a[contains(@class, 'add_to_cart_button')])[1]")
    SECOND_PRODUCT = (By.XPATH, "(//a[contains(@class, 'add_to_cart_button')])[2]")
    VIEW_CART_BUTTON = (By.XPATH, "//a[contains(@class, 'added_to_cart')]")
    CART_ICON = (By.CLASS_NAME, "cart-contents")
    
    def add_first_product_to_cart(self):
        self.click_element(self.FIRST_PRODUCT)
        time.sleep(3)  
    
    def add_second_product_to_cart(self):
        self.click_element(self.SECOND_PRODUCT)
        time.sleep(3)  
    
    def view_cart(self):
        try:
            self.click_element(self.VIEW_CART_BUTTON)
        except:
            self.click_element(self.CART_ICON)
        time.sleep(2)