import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    yield driver

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            driver.save_screenshot(
                screenshot_path
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