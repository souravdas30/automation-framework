from selenium.webdriver.common.by import By
from .base_page import BasePage

class AccountPage(BasePage):
    ADDRESSES_LINK = (By.LINK_TEXT, "Addresses")
    EDIT_BILLING_ADDRESS = (By.LINK_TEXT, "Edit")
    BILLING_FIRST_NAME = (By.ID, "billing_first_name")
    BILLING_LAST_NAME = (By.ID, "billing_last_name")
    BILLING_ADDRESS_1 = (By.ID, "billing_address_1")
    BILLING_CITY = (By.ID, "billing_city")
    BILLING_POSTCODE = (By.ID, "billing_postcode")
    BILLING_PHONE = (By.ID, "billing_phone")
    BILLING_EMAIL = (By.ID, "billing_email")
    SAVE_ADDRESS_BUTTON = (By.NAME, "save_address")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "woocommerce-message")
    
    def navigate_to_addresses(self):
        self.click_element(self.ADDRESSES_LINK)
    
    def edit_billing_address(self):
        self.click_element(self.EDIT_BILLING_ADDRESS)
    
    def save_address(self, address_data):
        if 'first_name' in address_data:
            self.enter_text(self.BILLING_FIRST_NAME, address_data['first_name'])
        if 'last_name' in address_data:
            self.enter_text(self.BILLING_LAST_NAME, address_data['last_name'])
        if 'address_1' in address_data:
            self.enter_text(self.BILLING_ADDRESS_1, address_data['address_1'])
        if 'city' in address_data:
            self.enter_text(self.BILLING_CITY, address_data['city'])
        if 'postcode' in address_data:
            self.enter_text(self.BILLING_POSTCODE, address_data['postcode'])
        if 'phone' in address_data:
            self.enter_text(self.BILLING_PHONE, address_data['phone'])
        if 'email' in address_data:
            self.enter_text(self.BILLING_EMAIL, address_data['email'])
        
        self.click_element(self.SAVE_ADDRESS_BUTTON)
    
    def is_address_saved_successfully(self):
        return self.is_element_visible(self.SUCCESS_MESSAGE)
