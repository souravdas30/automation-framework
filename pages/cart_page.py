from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "tr.cart_item")
    REMOVE_BUTTON = (By.CLASS_NAME, "remove")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "cart-empty")
    CONTINUE_SHOPPING = (By.LINK_TEXT, "Continue Shopping")
    
    def get_cart_items_count(self):
        try:
            return len(self.driver.find_elements(*self.CART_ITEMS))
        except:
            return 0
    
    def remove_first_item(self):
        if self.get_cart_items_count() > 0:
            self.click_element(self.REMOVE_BUTTON)
            time.sleep(3)  # Wait for removal
    
    def is_cart_empty(self):
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)
    
    def continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING)