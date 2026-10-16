import pytest
from pages.login_page import LoginPage
from utils.data_handler import load_config, load_test_data

def test_invalid_login_shows_error(driver):
    """Verifies that entering invalid credentials shows the correct error message."""
    config = load_config()
    test_data = load_test_data()
    
    invalid_credentials = test_data["invalid_user"]
    username = invalid_credentials["username"]
    password = invalid_credentials["password"]

    login_page = LoginPage(driver)
    login_page.open_url(config["base_url"])
    login_page.login(username, password)

    flash_message = login_page.get_flash_message_text()
    assert "Your username is invalid!" in flash_message, f"Expected error mismatch. Found: {flash_message}"


def test_valid_login_redirects_successfully(driver):
    """Verifies that entering correct credentials successfully logs the user in."""
    config = load_config()
    test_data = load_test_data()
    
    valid_credentials = test_data["valid_user"]
    
    login_page = LoginPage(driver)
    login_page.open_url(config["base_url"])
    login_page.login(valid_credentials["username"], valid_credentials["password"])
    
    flash_message = login_page.get_flash_message_text()
    assert "You logged into a secure area!" in flash_message, f"Expected login success mismatch. Found: {flash_message}"
