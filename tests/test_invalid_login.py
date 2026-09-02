from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils import constants

def test_login_with_invalid_credentials(browser):
    # Schritt 1: Cookies löschen und Homepage öffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)

    # Schritt 2: Erfolgreich einloggen initialisieren
    login_page = LoginPage(browser)
    login_page.click_profile()

    # Schritt 3: Ungültige Testdaten eingeben und absenden
    login_page.enter_username(constants.INVALID_USER)
    login_page.enter_password(constants.INVALID_PASSWORD)
    login_page.login_buton()

    # 🎯 الانتظار الكلاسيكي الشرعي: راجي لغاية ما كلمة Invalid تنزل وتظهر لداخل كود الـ HTML حاف
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid')]"))
    )

    # Schritt 4: Verifikation - Sicherstellen, dass die Fehlermeldung erscheint
    assert "Invalid" in browser.page_source
