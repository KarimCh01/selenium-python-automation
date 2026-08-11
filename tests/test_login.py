import pytest

from config.config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_url,expected_error",
    [
        (
            STANDARD_USERNAME,
            STANDARD_PASSWORD,
            BASE_URL + "inventory.html",
            None
        ),
        (
            "KARIM",
            "PASSWORDD",
            BASE_URL,
            "Epic sadface: Username and password do not match any user in this service"
        ),
    ]
)

@pytest.mark.smoke
def test_login(
    driver,
    username,
    password,
    expected_url,
    expected_error
):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )

    assert driver.current_url == expected_url

    if expected_error:
        assert login_page.get_error_message() == expected_error