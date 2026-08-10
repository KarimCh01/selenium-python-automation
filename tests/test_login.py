from pages.login_page import LoginPage

def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert driver.current_url =="https://www.saucedemo.com/inventory.html"

def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("KARIM", "PASSWORDD")

    assert login_page.get_error_message() == \
        "Epic sadface: Username and password do not match any user in this service"

    assert driver.current_url =="https://www.saucedemo.com/"


