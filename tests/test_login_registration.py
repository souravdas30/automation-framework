import pytest
import time
from selenium.webdriver.common.by import By
import random

class TestLoginRegistration:
    
    @pytest.mark.positive
    @pytest.mark.registration
    def test_user_registration(self, browser):
        """Test user registration page navigation"""
        print("Testing: User registration page")
        
        # Navigate to registration page
        browser.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        
        # Check if we're on registration page
        assert "my-account" in browser.current_url
        print("On My Account page")
        
        # Find registration form
        email_field = browser.find_element(By.ID, "reg_email")
        password_field = browser.find_element(By.ID, "reg_password")
        register_button = browser.find_element(By.NAME, "register")
        
        # Test form interaction
        random_email = f"test{random.randint(1000,9999)}@test.com"
        email_field.send_keys(random_email)
        password_field.send_keys("TestPassword123!")
        register_button.click()
        time.sleep(3)
        
        print("Registration form submitted successfully")

    @pytest.mark.negative
    @pytest.mark.registration
    def test_registration_with_invalid_email(self, browser):
        """Test registration form with invalid email"""
        print("Testing: Registration with invalid email")
        
        browser.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        
        # Try invalid email
        email_field = browser.find_element(By.ID, "reg_email")
        password_field = browser.find_element(By.ID, "reg_password")
        register_button = browser.find_element(By.NAME, "register")
        
        email_field.send_keys("invalid-email")
        password_field.send_keys("TestPassword123!")
        register_button.click()
        time.sleep(2)
        
        print("Submitted form with invalid email")

    @pytest.mark.positive
    @pytest.mark.login
    def test_successful_login_form(self, browser):
        """Test login form navigation"""
        print("Testing: Login form")
        
        browser.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        
        # Find login form
        username_field = browser.find_element(By.ID, "username")
        password_field = browser.find_element(By.ID, "password")
        login_button = browser.find_element(By.NAME, "login")
        
        # Test form interaction
        username_field.send_keys("test@example.com")
        password_field.send_keys("password123")
        login_button.click()
        time.sleep(2)
        
        print("Login form submitted successfully")

    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_invalid_credentials(self, browser):
        """Test login with invalid credentials"""
        print("Testing: Login with invalid credentials")
        
        browser.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        
        # Use invalid credentials
        browser.find_element(By.ID, "username").send_keys("invalid_user@example.com")
        browser.find_element(By.ID, "password").send_keys("WrongPassword123!")
        browser.find_element(By.NAME, "login").click()
        time.sleep(2)
        
        print("Submitted invalid login credentials")