from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    TITLE=(By.CSS_SELECTOR,'[data-test="title"]')
    PRODUCT_NAME =(By.CSS_SELECTOR,'[data-test="inventory-item-name"]')
    CHECKOUT_BUTTON = (By.ID,"checkout")

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def get_title(self):

        title=self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return title.text

    def get_product_name(self):
        product=self.wait.until(

        EC.visibility_of_element_located(self.PRODUCT_NAME)
        )
        return product.text

    def click_checkout(self):
        check_button =self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        check_button.click()