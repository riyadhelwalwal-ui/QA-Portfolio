
from pages.login_page import LoginPage
from utils import constants


def test_login_with_invalid_credentials(browser):
    # Schritt 1: Cookies löschen und Homepage öffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)


    # Schritt 2: Login-Seite öffnen
    login_page = LoginPage(browser)
    login_page.click_profile()


    # Schritt 3: Ungültige Testdaten eingeben und absenden
    login_page.enter_username(constants.INVALID_USER)
    login_page.enter_password(constants.INVALID_PASSWORD)
    login_page.login_buton()


    # Schritt 4: Verifikation - Sicherstellen, dass die Fehlermeldung erscheint
    assert "Invalid" in browser.page_source or "error" in browser.page_source.lower()
