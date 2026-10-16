import os
import sys
import pytest

# Core Fix: Dynamically append the project root directory to Python's system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Internal imports must happen AFTER the path is injected
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from utils.data_handler import load_config

@pytest.fixture(scope="function")
def driver():
    """Initializes the specific web browser driver based on configuration values.
    
    Tears down and quits the driver session automatically when a test finishes execution.
    """
    config = load_config()
    browser_type = config.get("browser", "chrome").lower()
    timeout = config.get("timeout", 10)
    
    if browser_type == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
    elif browser_type == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
    else:
        raise ValueError(f"Browser type '{browser_type}' is not supported by this framework.")

    driver.implicitly_wait(timeout)
    driver.maximize_window()

    yield driver
    driver.quit()
