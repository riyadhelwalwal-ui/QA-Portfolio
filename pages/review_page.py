from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import constants


class ReviewPage:
    def __init__(self, driver):
        self.driver = driver

        # --- Element-Lokatoren (Checkout & Review) ---
        self.street_input = (By.XPATH, "//input[@placeholder='Street Address']")
        self.city_input = (By.XPATH, "//input[@placeholder='City']")
        self.zip_input = (By.XPATH, "//input[@placeholder='Postal Code']")
        self.card_input = (By.XPATH, "//input[@placeholder='Card number']")
        self.name_input = (By.XPATH, "//input[@placeholder='Name on card']")
        self.exp_input = (By.XPATH, "//input[@placeholder='Expiration']")
        self.cvv_input = (By.XPATH, "//input[@placeholder='Cvv']")
        self.buy_now_btn = (By.XPATH, "//button[text()='Buy now']")

        # Produktlink auf der Homepage nach dem Kauf
        self.gala_apples_link = (By.XPATH, "//img[@alt='Gala Apples']")


        # Review-Eingabefeld und Absendebutton (Nach der Live-Oberfläche)
        self.review_textarea = (By.XPATH, "//textarea[@placeholder='What is your view?']")
        self.submit_review_btn = (By.XPATH, "//button[contains(text(), 'Send')]")

    # --- Seiten-Aktionen ---
    def fill_checkout_and_buy(self):
        # Dummy-Daten eingeben fuer den Checkout-Prozess
        self.driver.find_element(*self.street_input).send_keys("Hauptstrasse 10")
        self.driver.find_element(*self.city_input).send_keys("Berlin")
        self.driver.find_element(*self.zip_input).send_keys("10783")
        self.driver.find_element(*self.name_input).send_keys("Riyad QA")
        self.driver.find_element(*self.exp_input).send_keys("12/2029")

        # Sensitive Daten aus constants.py abrufen
        self.driver.find_element(*self.card_input).send_keys(constants.FAKE_CARD)
        self.driver.find_element(*self.cvv_input).send_keys(constants.FAKE_CVV)
        self.driver.find_element(*self.buy_now_btn).click()

    def open_gala_product_page(self):
        # Produktseite von Gala Apples erneut oeffnen
        self.driver.find_element(*self.gala_apples_link).click()

    def enter_review_text(self, text):
        # Langen Text in das Review-Feld eingeben
        self.driver.find_element(*self.review_textarea).send_keys(str(text))

    def get_text_lange(self):
        element = self.driver.find_element(*self.review_textarea)
        return len(element.get_attribute("value"))

    def click_submit_review(self):
        # Review absenden
        self.driver.find_element(*self.submit_review_btn).click()
