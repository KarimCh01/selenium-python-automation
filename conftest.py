import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption(
        "--browser"
    )

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        # SauceDemo's checkout form looks like an address form to Chrome,
        # which can pop up autofill suggestions that steal focus mid-test.
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        })

        driver = webdriver.Chrome(
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(
            options=options
        )

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    yield driver

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            driver.save_screenshot(
                f"screenshots/{request.node.name}.png"
            )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )