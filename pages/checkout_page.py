from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    def get_title(self):
        return self.get_text(self.TITLE)

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.type_text(
            self.FIRST_NAME,
            first_name
        )

        self.type_text(
            self.LAST_NAME,
            last_name
        )

        self.type_text(
            self.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

        self.wait_for_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )