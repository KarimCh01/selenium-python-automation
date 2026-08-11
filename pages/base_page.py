from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(
            self.__class__.__name__
        )

    def click(self, locator):
        self.logger.info(
            f"Clicking element: {locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def type_text(self, locator, text, attempts=2):
        self.logger.info(
            f"Typing into element: {locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        retry_wait = WebDriverWait(self.driver, 2)

        for attempt in range(attempts):
            # Only clear when there's something to clear: calling
            # clear() on an already-empty field can briefly steal focus
            # in headless Chrome, causing the keystrokes below to be
            # dropped.
            if element.get_attribute("value"):
                element.clear()

            element.send_keys(text)

            try:
                retry_wait.until(
                    lambda driver:
                    driver.find_element(*locator).get_attribute("value") == text
                )
                return
            except TimeoutException:
                element = self.driver.find_element(*locator)

        # Headless Chrome occasionally drops native key events for a
        # field entirely. As a last resort, insert the text the way the
        # browser itself would (paste/autofill) and confirm it landed.
        element.click()

        self.driver.execute_script(
            "document.execCommand('insertText', false, arguments[0]);",
            text
        )

        self.wait.until(
            lambda driver:
            driver.find_element(*locator).get_attribute("value") == text
        )

    def get_text(self, locator):
        self.logger.info(
            f"Getting text from element: {locator}"
        )

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_for_url(self, url):
        self.logger.info(
            f"Waiting for URL: {url}"
        )

        self.wait.until(
            EC.url_to_be(url)
        )

    def click_and_wait_for_url(self, locator, url_fragment, attempts=3):
        for attempt in range(attempts):
            self.click(locator)

            try:
                self.wait.until(
                    EC.url_contains(url_fragment)
                )
                return
            except TimeoutException:
                # Headless Chrome occasionally drops a click entirely.
                # A full wait has already confirmed nothing happened, so
                # re-clicking the (still present) element is safe.
                if attempt == attempts - 1:
                    raise