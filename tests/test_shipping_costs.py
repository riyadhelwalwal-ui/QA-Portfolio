import time
from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shipping_page import ShippingPage
from utils import constants


def test_shipping_free_at_20_euro(browser):
    # Schritt 1: Cookies loeschen für eine saubere Testumgebung
    browser.delete_all_cookies()

    # Schritt 2: Homepage oeffnen
    browser.get(constants.BASE_URL)
    time.sleep(2)

    # Schritt 3: Einloggen (Account Icon und Daten eingeben)
    login_page = LoginPage(browser)
    login_page.click_profile()
    time.sleep(2)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()
    time.sleep(4)

    # Schritt 4: Auf die Shop-Schaltflaeche klicken
    login_page.enter_shop()
    time.sleep(3)

    # Schritt 5: Altersverifikation ausfuellen
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()
    time.sleep(3)

    # Schritt 6: Gala Apples auf 10 setzen (20€) und zum Checkout gehen
    shipping_page = ShippingPage(browser)
    shipping_page.enter_apples_quantity("0")

    time.sleep(1)
    shipping_page.click_add_to_cart()
    time.sleep(2)
    browser.refresh()
    time.sleep(2)
    shipping_page.go_to_checkout()
    time.sleep(4)

    # Schritt 7: Verifikation - überprüfen, ob der Logik-Bug existiert
    assert "Free shipment if your purchase is 20€ or more." in browser.page_source
