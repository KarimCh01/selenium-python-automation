from selenium import webdriver  # Import WebDriver so Selenium can control the browser

from selenium.webdriver.common.by import By  # Import By so Selenium can find HTML elements using ID, NAME, XPath, CSS, etc.


def test_google_search():  # Pytest recognizes this as a test because the function starts with test_

    driver = webdriver.Chrome()  # Create a Chrome browser session controlled by Selenium

    driver.get("https://www.google.com")  # Tell Selenium to open this URL in the browser


    search_box = driver.find_element(By.NAME, "q")
    # Find ONE HTML element whose name="q"
    # Google uses name="q" for its search box
    # Store the found HTML element inside the search_box variable


    search_box.send_keys("Selenium Python")
    # Type "Selenium Python" inside the HTML element stored in search_box
    # This is an ACTION performed by Selenium


    assert search_box.get_attribute("value") == "Selenium Python"
    # Get the current "value" from the search box
    # Compare the ACTUAL value with the EXPECTED value "Selenium Python"
    # If they are equal -> test PASSES
    # If they are different -> test FAILS


    driver.quit()
    # Close the entire Chrome browser session