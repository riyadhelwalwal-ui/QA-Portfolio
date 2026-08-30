from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgePage:
    def __init__(self, driver):
        self.driver = driver

        # --- Element-Lokatoren (Altersverifikation) ---
        self.age_input = (By.XPATH, "//div[contains(@class, 'modal')]//input | //input[@placeholder='DD-mm-YYYY']")
        self.confirm_button = (By.XPATH, "//button[text()='Confirm']")

    # --- Seiten-Aktionen ---
    def enter_birthdate(self, date_str):
        # Warten, bis das Eingabefeld sichtbar und klickbar ist (max. 10 Sekunden)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.age_input)
        )
        element.click()  # Feld aktivieren
        element.clear()  # Feld leeren
        element.send_keys(str(date_str))  # Geburtsdatum als String eingeben

    def click_confirm(self):
        # Warten, bis die Schaltflaeche "Confirm" klickbar ist
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_button)
        )
        button.click()
