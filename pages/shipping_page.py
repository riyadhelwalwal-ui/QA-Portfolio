from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShippingPage:
    def __init__(self, driver):
        self.driver = driver

        # --- Element-Lokatoren (Gala Apples & Cart) ---
        self.apples_qty = (By.XPATH, "//div[contains(., 'Gala Apples')]/following-sibling::div//input[@type='number']")
        self.add_to_cart_btn = (By.XPATH, "//div[contains(., 'Gala Apples')]/following-sibling::div//button[contains(text(), 'Add to Cart')]")
        self.cart_icon = (By.XPATH, "(//div[@class='headerIcon'][3])")

    # --- Seiten-Aktionen ---
    def enter_apples_quantity(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apples_qty)
        )
        element.click()
        element.send_keys("0")

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_checkout(self):
        self.driver.find_element(*self.cart_icon).click()
