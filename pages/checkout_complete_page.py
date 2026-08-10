from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return title.text

    def click_finish(self):
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        finish_button.click()

    def get_complete_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )
        return message.text