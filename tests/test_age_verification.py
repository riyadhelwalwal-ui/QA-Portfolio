from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shop_page import ShopPage
from utils import constants


def test_age_verification_1987(browser):
    # Schritt 1: Cookies loeschen und Homepage oeffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)

    # Schritt 2: Profil oeffnen und einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()

    # Schritt 3: Shop oeffnen (صناعة الكائن بالاسم الصغير أولاً)
    shop_page = ShopPage(browser)
    shop_page.enter_shop()

    # Schritt 4: Altersverifikation mit Geburtsjahr 1987 ausfuehren
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()

    # Schritt 5: Verifikation - Sicherstellen, dass Fehlermeldung NICHT erscheint
    assert "You are underage" not in  browser.page_source
