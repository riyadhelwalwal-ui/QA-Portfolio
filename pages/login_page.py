from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Zentraler Explicit Wait (15 Sekunden Sicherheitslimit)
        self.wait = WebDriverWait(self.driver, 15)

        # Stabile Locators nach der Profil-XPath-Korrektur
        self.profile_icon = (By.XPATH, "(//div[@class='headerIcon'])[1]")
        self.username_input = (By.XPATH, "//input[@type='email']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button_element = (By.XPATH, "//button[@type='submit']")

    def click_profile(self):
        # Wartet, bis das Profil-Icon im DOM vorhanden ist, und klickt darauf
        element = self.wait.until(EC.presence_of_element_located(self.profile_icon))
        element.click()

    def enter_username(self, username):
        # Wartet auf das Eingabefeld und traegt den Benutzernamen ein
        element = self.wait.until(EC.presence_of_element_located(self.username_input))
        element.send_keys(username)

    def enter_password(self, password):
        # Direkte Eingabe zur Optimierung der Testgeschwindigkeit
        self.driver.find_element(*self.password_input).send_keys(password)

    def login_buton(self):
        # Fuehrt den Login-Klick direkt aus
        self.driver.find_element(*self.login_button_element).click()