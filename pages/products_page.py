from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class ProductsPage(BasePage):

    TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    PRODUCTS = (
        By.CSS_SELECTOR,
        '[data-test="inventory-item-name"]'
    )

    SORT_DROPDOWN = (
        By.CSS_SELECTOR,
        '[data-test="product-sort-container"]'
    )

    PRICES = (
        By.CSS_SELECTOR,
        '[data-test="inventory-item-price"]'
    )

    ADD_BIKE_LIGHT = (
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    )

    CART_BADGE = (
        By.CSS_SELECTOR,
        '[data-test="shopping-cart-badge"]'
    )

    CART_LINK = (
        By.CSS_SELECTOR,
        '[data-test="shopping-cart-link"]'
    )

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_product_count(self):
        products = self.find_all(self.PRODUCTS)
        return len(products)

    def sort_by_price_low_to_high(self):
        dropdown = self.find(self.SORT_DROPDOWN)

        Select(dropdown).select_by_visible_text(
            "Price (low to high)"
        )

    def get_prices(self):
        prices = self.find_all(self.PRICES)

        return [
            float(price.text.replace("$", ""))
            for price in prices
        ]

    def add_bike_light_to_cart(self):
        self.click(self.ADD_BIKE_LIGHT)

    def get_cart_badge(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

        self.wait_for_url(
            "https://www.saucedemo.com/cart.html"
        )