from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return title.text


    def enter_customer_information(self, first_name, last_name, postal_code):
        first_name_element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        first_name_element.send_keys(first_name)

        last_name_element = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        last_name_element.send_keys(last_name)

        postal_code_element = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )
        postal_code_element.send_keys(postal_code)


    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()