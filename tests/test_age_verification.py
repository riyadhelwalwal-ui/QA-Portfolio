import time
from pages.login_page import LoginPage
from pages.age_page import AgePage
from utils import constants


def test_age_verification_1987(browser):
    # Schritt 1: Cookies loeschen für eine saubere Testumgebung
    browser.delete_all_cookies()

    # Schritt 2: Homepage oeffnen und die Seite aktualisieren
    browser.get(constants.BASE_URL)
    browser.refresh()
    time.sleep(3)

    # Schritt 3: Account-Icon klicken und erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    time.sleep(2)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()
    time.sleep(4)

    # Schritt 4: Auf die Schaltflaeche "Shop" klicken
    login_page.enter_shop()
    time.sleep(3)

    # Schritt 5: Geburtsdatum eingeben und auf "Confirm" klicken
    age_page = AgePage(browser)
    age_page.enter_birthdate("01.05.1987")
    age_page.click_confirm()
    time.sleep(3)

    # Schritt 6: Verifikation - Überprüfen, ob der Bug existiert und "You are underage" erscheint
    assert "You are underage" not in browser.page_source


