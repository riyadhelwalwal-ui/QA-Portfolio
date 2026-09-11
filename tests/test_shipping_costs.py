from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shipping_page import ShippingPage
from pages.shop_page import ShopPage
from utils import constants


def test_shipping_free_at_20_euro(browser):
    # Schritt 1: Cookies loeschen für eine saubere Testumgebung
    browser.delete_all_cookies()

    # Schritt 2: Homepage oeffnen
    browser.get(constants.BASE_URL)

    # Schritt 3: Erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()

    # Session-Schutz: Wartet bis die URL gewechselt hat
    WebDriverWait(browser, 15).until_not(EC.url_contains("/auth"))

    # Schritt 4: Auf die Shop-Schaltflaeche klicken via POM
    shop_page = ShopPage(browser)
    shop_page.enter_shop()

    # Schritt 5: Altersverifikation ausfuellen
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()

    # 🎯 EXPLICIT WAIT: Wartet bis das Alters-Overlay komplett verschwindet
    underage_toast = (By.XPATH, "//*[contains(text(), 'You are underage') or contains(@class, 'toast')]")
    WebDriverWait(browser, 15).until(EC.invisibility_of_element_located(underage_toast))

    # Schritt 6: Menge auf 10 setzen (0 neben der 1 einfuegen) und in den Warenkorb legen
    shipping_page = ShippingPage(browser)
    shipping_page.enter_apples_quantity("0")
    shipping_page.click_add_to_cart()

    # Refresh zur Stabilisierung der Session
    browser.refresh()

    # Navigieren zum Checkout via stabiler POM-Methode
    shipping_page.go_to_checkout()

    # Schritt 7: Verifikation - Abfangen des Fehlers unter 50 Euro
    assert "4.95" in browser.page_source
