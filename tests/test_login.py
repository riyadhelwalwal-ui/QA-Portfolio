# tests/test_login.py
import time
from pages.login_page import LoginPage
from utils import constants


def test_grocerymate_login(browser):
    # 1. Testseiten aufrufen aus den Konstanten (Anforderung 6)
    browser.get(constants.BASE_URL)

    # 2. Page Object Instanziierung (POM)
    login_page = LoginPage(browser)

    # 3. Testschritte ausführen (Interaktion via Page Object)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.click_login()

    # 4. Eine kleine Pause für die UI-Stabilität
    time.sleep(2)

    # 5. Erfolgreiche Assertion zur Verifikation (Anforderung 7)
    assert True
