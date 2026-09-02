from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shipping_page import ShippingPage
from pages.review_page import ReviewPage
from utils import constants

def test_review_character_limit_bug(browser):
    # Schritt 1: Cookies löschen und Homepage öffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)

    # Schritt 2: Erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()

    # Schritt 3: Shop öffnen und Altersverifikation ausfüllen
    login_page.enter_shop()
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()

    # Schritt 4: Ein Produkt in den Warenkorb legen und zum Checkout wechseln
    shipping_page = ShippingPage(browser)
    shipping_page.click_add_to_cart()
    shipping_page.go_to_checkout()

    # Schritt 5: Checkout-Formular ausfüllen und Bestellung bestätigen
    shipping_page.fill_checkout_and_buy()

    # 🎯 لقطة القبطان السحرية: دير ريفريش عشان تطير البوب أب والواجهة الشفافة في ثانية
    browser.refresh()

    # Schritt 5b: Shop erneut oeffnen (توا ح يضغط طيران وبدون أي كراش)
    login_page.enter_shop()

    # Schritt 5c: Zurueck zur Produktseite von Gala Apples wechseln
    review_page = ReviewPage(browser)
    review_page.open_gala_product_page()

    # Schritt 6: Review-Text mit über 500 Zeichen eingeben
    review_page.enter_review_text(constants.BUG_REVIEW_TEXT)

    # Schritt 7: Verifikation - Sicherstellen, dass das System exakt bei 500 Zeichen blockiert
    actual_length = review_page.get_text_lange()
    assert actual_length == 500
