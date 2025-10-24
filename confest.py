import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture(scope="function")
def browser():
    print("Starting browser...")
    
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=options
        )
        
        driver.implicitly_wait(10)
        
        driver.get("https://practice.automationtesting.in/")
        time.sleep(3)  # Wait for page to load
        
        print(" Website loaded successfully")
        yield driver
        
    except Exception as e:
        print(f"Browser setup failed: {e}")
        pytest.fail(f"Browser setup failed: {e}")
    
    finally:
        try:
            driver.quit()
            print("Browser closed")
        except:
            pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)