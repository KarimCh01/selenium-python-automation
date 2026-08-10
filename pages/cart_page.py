from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        '[data-test="inventory-item-name"]'
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

