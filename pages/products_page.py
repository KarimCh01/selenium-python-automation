from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    PRODUCTS = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    PRICES = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def __init__(self, driver):
        self.driver = driver #Saves the browser
        self.wait = WebDriverWait(driver, 10) #Saves a 10-second wait that uses that browser

    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return title.text

    def get_product_count(self):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCTS)
        )
        return len(products)

    def sort_by_price_low_to_high(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_visible_text("Price (low to high)")

    def get_prices(self):
        prices = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRICES)
        )
        return [
            float(price.text.replace("$", ""))
            for price in prices
        ]

    def add_bike_light_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BIKE_LIGHT)
        )
        button.click()

    def get_cart_badge(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def open_cart(self):
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart.click()