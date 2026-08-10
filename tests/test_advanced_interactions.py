from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert(driver):
    driver.get(
        "https://the-internet.herokuapp.com/javascript_alerts"
    )

    alert_button = driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Alert']"
    )

    alert_button.click()

    alert = driver.switch_to.alert

    assert alert.text == "I am a JS Alert"

    alert.accept()


def test_iframe(driver):
    driver.get(
        "https://the-internet.herokuapp.com/iframe"
    )

    iframe = driver.find_element(
        By.ID,
        "mce_0_ifr"
    )

    driver.switch_to.frame(iframe)

    editor = driver.find_element(
        By.ID,
        "tinymce"
    )

    assert editor.is_displayed()

    driver.switch_to.default_content()


def test_new_tab(driver):
    driver.get(
        "https://the-internet.herokuapp.com/windows"
    )

    original_tab = driver.current_window_handle

    driver.find_element(
        By.LINK_TEXT,
        "Click Here"
    ).click()

    all_tabs = driver.window_handles

    driver.switch_to.window(
        all_tabs[1]
    )

    title = driver.find_element(
        By.TAG_NAME,
        "h3"
    )

    assert title.text == "New Window"

    driver.close()

    driver.switch_to.window(
        original_tab
    )


def test_hover(driver):
    driver.get(
        "https://the-internet.herokuapp.com/hovers"
    )

    users = driver.find_elements(
        By.CLASS_NAME,
        "figure"
    )

    first_user = users[0]

    actions = ActionChains(driver)

    actions.move_to_element(
        first_user
    ).perform()

    captions = driver.find_elements(
        By.CLASS_NAME,
        "figcaption"
    )

    first_caption = captions[0]

    assert first_caption.is_displayed()


def test_file_upload(driver, tmp_path):
    driver.get(
        "https://the-internet.herokuapp.com/upload"
    )

    test_file = tmp_path / "test.txt"

    test_file.write_text(
        "Hello Selenium"
    )

    upload_input = driver.find_element(
        By.ID,
        "file-upload"
    )

    upload_input.send_keys(
        str(test_file)
    )

    assert "test.txt" in upload_input.get_attribute(
        "value"
    )


def test_dynamic_element(driver):
    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/1"
    )

    start_button = driver.find_element(
        By.TAG_NAME,
        "button"
    )

    start_button.click()

    hello_text = WebDriverWait(
        driver,
        10
    ).until(
        EC.visibility_of_element_located(
            (By.ID, "finish")
        )
    )

    assert hello_text.text == "Hello World!"