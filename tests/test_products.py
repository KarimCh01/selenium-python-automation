from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


def login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")


def test_products_are_displayed(driver):
    login(driver) #Open SauceDemo -> enter username/password -> click Login.

    products_page = ProductsPage(driver)

    assert products_page.get_title() == "Products"
    assert products_page.get_product_count() == 6


def test_products_can_be_sorted_by_price(driver):
    login(driver)

    products_page = ProductsPage(driver)

    products_page.sort_by_price_low_to_high()

    price_values = products_page.get_prices()

    assert price_values == sorted(price_values)


def test_product_can_be_added_to_cart(driver):
    login(driver)

    products_page = ProductsPage(driver)

    products_page.add_bike_light_to_cart()

    assert products_page.get_cart_badge() == "1"

    products_page.open_cart()

    assert driver.current_url == "https://www.saucedemo.com/cart.html"

def test_product_can_be_added_to_cart(driver):
    login(driver)

    products_page=ProductsPage(driver)
    products_page.add_bike_light_to_cart()
    assert products_page.get_cart_badge() =="1"

    products_page.open_cart()
    assert driver.current_url =="https://www.saucedemo.com/cart.html"

    cart_page=CartPage(driver) #Products -> Cart, you're not opening another browser. You're creating another Python object that controls the same browser/session.

    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_product_name() == "Sauce Labs Bike Light"

def test_user_can_enter_checkout_information(driver):
    login(driver)

    products_page = ProductsPage(driver)
    products_page.add_bike_light_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    assert checkout_page.get_title() == "Checkout: Your Information"

    checkout_page.enter_customer_information(
        "Karim",
        "Chehab",
        "12345"
    )

    checkout_page.click_continue()

    assert driver.current_url == \
        "https://www.saucedemo.com/checkout-step-two.html"


def test_complete_checkout(driver):
    login(driver)

    products_page = ProductsPage(driver)
    products_page.add_bike_light_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_information(
        "Karim",
        "Chehab",
        "12345"
    )
    checkout_page.click_continue()

    complete_page = CheckoutCompletePage(driver)

    assert complete_page.get_title() == "Checkout: Overview"

    complete_page.click_finish()

    assert complete_page.get_complete_message() == "Thank you for your order!"