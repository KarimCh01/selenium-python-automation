import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_url,expected_error",
    [
        (
            "standard_user",
            "secret_sauce",
            "https://www.saucedemo.com/inventory.html",
            None
        ),
        (
            "KARIM",
            "PASSWORDD",
            "https://www.saucedemo.com/",
            "Epic sadface: Username and password do not match any user in this service"
        ),
    ]
)
def test_login(
    driver,
    username,
    password,
    expected_url,
    expected_error
):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )

    assert driver.current_url == expected_url

    if expected_error:
        assert login_page.get_error_message() == expected_error