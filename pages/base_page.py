from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        """Navigates to the specified URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Waits for an element to be present in the DOM and returns it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Waits for an element to be clickable and clicks it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Waits for an input field, clears it, and inputs text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        """Returns the current page title."""
        return self.driver.title
