from pages.login_page import LoginPage
from utils import constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_grocerymate_login(browser):
    # Schritt 1: Homepage oeffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)

    # Schritt 2: Erfolgreichen Login ausfuehren
    login_page = LoginPage(browser)
    login_page.click_profile()
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()

    WebDriverWait(browser, 10).until_not(EC.url_contains("/auth"))


    # Schritt 3: Verifikation -  /auth hat verlassen

    assert "/auth" not in browser.current_url
