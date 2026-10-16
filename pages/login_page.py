from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators matching the live site elements
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Performs login action step-by-step using base page wrappers."""
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_flash_message_text(self):
        """Retrieves confirmation message or banner error responses."""
        return self.find_element(self.FLASH_MESSAGE).text
