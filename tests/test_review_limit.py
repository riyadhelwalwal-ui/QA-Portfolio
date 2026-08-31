import time
from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shipping_page import ShippingPage
from pages.review_page import ReviewPage
from utils import constants


def test_review_character_limit_bug(browser):
    # Schritt 1: Cookies loeschen und Homepage oeffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)
    time.sleep(2)

    # Schritt 2: Erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    time.sleep(2)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()
    time.sleep(4)

    # Schritt 3: Shop oeffnen und Altersverifikation ausfuellen
    login_page.enter_shop()
    time.sleep(3)
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()
    time.sleep(3)

    # Schritt 4: Ein Produkt in den Warenkorb legen und zum Checkout wechseln
    shipping_page = ShippingPage(browser)
    shipping_page.click_add_to_cart()
    time.sleep(2)
    shipping_page.go_to_checkout()
    time.sleep(4)

    # Schritt 5: Checkout-Formular ausfuellen und Bestellung bestaetigen
    review_page = ReviewPage(browser)
    review_page.fill_checkout_and_buy()
    time.sleep(4)

    # Schritt 5b: Shop erneut oeffnen, um zur Produktliste zu gelangen
    login_page.enter_shop()
    time.sleep(4)

    # Schritt 5c: Zurueck zur Produktseite von Gala Apples wechseln
    review_page.open_gala_product_page()
    time.sleep(4)

    # Schritt 6: Review-Text mit ueber 500 Zeichen eingeben
    review_page.enter_review_text(constants.BUG_REVIEW_TEXT)
    time.sleep(2)

    # Schritt 7: Verifikation - Sicherstellen, dass das System exakt bei 500 Zeichen blockiert
    actual_length = review_page.get_text_lange()
    assert actual_length == 500
