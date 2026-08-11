from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    COMPLETE_HEADER = (
        By.CSS_SELECTOR,
        '[data-test="complete-header"]'
    )

    def get_title(self):
        return self.get_text(self.TITLE)

    def click_finish(self):
        self.click_and_wait_for_url(
            self.FINISH_BUTTON,
            "checkout-complete.html"
        )

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)