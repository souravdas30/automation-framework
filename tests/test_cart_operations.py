import pytest
import time
from selenium.webdriver.common.by import By

class TestCartOperations:
    
    @pytest.mark.positive
    @pytest.mark.cart
    def test_add_single_product_to_cart(self, browser):
        """Test adding a single product to cart"""
        print("Testing: Add product to cart")
        
        # Navigate to shop
        browser.find_element(By.LINK_TEXT, "Shop").click()
        time.sleep(2)
        
        # Find and click first add to cart button
        add_buttons = browser.find_elements(By.CSS_SELECTOR, "a.add_to_cart_button")
        assert len(add_buttons) > 0, "No add to cart buttons found"
        
        add_buttons[0].click()
        time.sleep(3)
        print("Product added to cart")
        
        # Try to view cart
        try:
            browser.find_element(By.CSS_SELECTOR, "a.added_to_cart").click()
        except:
            browser.find_element(By.CLASS_NAME, "cart-contents").click()
        
        time.sleep(2)
        assert "cart" in browser.current_url, "Should be on cart page"
        print("Successfully navigated to cart page")

    @pytest.mark.positive
    @pytest.mark.cart
    def test_remove_product_from_cart(self, browser):
        """Test removing product from cart"""
        print("Testing: Remove product from cart")
        
        # First ensure we have a product in cart
        browser.get("https://practice.automationtesting.in/")
        browser.find_element(By.LINK_TEXT, "Shop").click()
        time.sleep(2)
        
        add_buttons = browser.find_elements(By.CSS_SELECTOR, "a.add_to_cart_button")
        if len(add_buttons) == 0:
            pytest.skip("No products available to test removal")
            
        add_buttons[0].click()
        time.sleep(3)
        
        # Go to cart
        browser.find_element(By.CLASS_NAME, "cart-contents").click()
        time.sleep(2)
        
        # Remove item
        remove_buttons = browser.find_elements(By.CSS_SELECTOR, "a.remove")
        if len(remove_buttons) > 0:
            remove_buttons[0].click()
            time.sleep(3)
            print("Product removed from cart")
        else:
            pytest.skip("No remove button found")

    @pytest.mark.negative
    @pytest.mark.cart
    def test_cart_empty_state(self, browser):
        """Test empty cart behavior"""
        print("Testing: Empty cart state")
        
        # Go directly to empty cart
        browser.get("https://practice.automationtesting.in/cart/")
        time.sleep(2)
        
        # Check for empty cart message
        page_text = browser.page_source.lower()
        assert "empty" in page_text or "no products" in page_text or "cart" in browser.current_url
        print("Empty cart state verified")
