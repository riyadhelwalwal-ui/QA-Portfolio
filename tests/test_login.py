# tests/test_login.py
from selenium import webdriver
from pages.login_page import LoginPage
from utils import constants


def test_grocerymate_login():
    # 1. WebDriver Initialisierung (Anforderung 4)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implizites Warten auf UI-Elemente (Anforderung 5)

    # 2. Testseiten aufrufen aus den Konstanten (Anforderung 6)
    driver.get(constants.BASE_URL)

    # 3. Page Object Instanziierung (POM)
    login_page = LoginPage(driver)

    # 4. Testschritte ausführen (Interaktion via Page Object)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.click_login()

    # 5. Browser-Sitzung ordnungsgemäß beenden
    driver.quit()
