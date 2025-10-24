# UI Automation Framework

A comprehensive Selenium WebDriver based automation framework for testing the automation practice website.

## Framework Overview

This framework is built using:
- **Selenium WebDriver**: For browser automation
- **Python**: Programming language
- **Pytest**: Test framework
- **Page Object Model**: Design pattern for maintainable tests

## Test Cases Coverage

### Cart Operations Tests

#### Positive Test Cases:
1. **test_add_single_product_to_cart**: Verify adding a single product to cart
2. **test_add_multiple_products_to_cart**: Verify adding multiple products to cart  
3. **test_remove_product_from_cart**: Verify removing product from cart

#### Negative Test Cases:
1. **test_cart_empty_state**: Verify empty cart behavior and messages

### Login & Registration Tests

#### Positive Test Cases:
1. **test_user_registration**: Verify successful user registration
2. **test_successful_login**: Verify login with valid credentials

#### Negative Test Cases:
1. **test_registration_with_invalid_email**: Verify registration fails with invalid email
2. **test_registration_with_weak_password**: Verify registration fails with weak password
3. **test_login_with_invalid_credentials**: Verify login fails with invalid credentials

### Address Management Tests
#### Positive Test Cases:
1. **test_add_billing_address**: Verify adding billing address to profile
2. **test_verify_address_saved_correctly**: Verify address details are saved correctly

#### Negative Test Cases:
1. **test_address_with_missing_required_fields**: Verify validation for required address fields

## Project Structure