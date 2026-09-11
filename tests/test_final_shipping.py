import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.shipping_page import ShippingPage
from pages.age_page import AgePage
from pages.shop_page import ShopPage
from utils import constants


def test_shipping_costs_validation(browser):
    # Schritt 1: Cookies loeschen und Homepage oeffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)

    # Schritt 2: Erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()

    # Schritt 3: Shop oeffnen via POM
    shop_page = ShopPage(browser)
    shop_page.enter_shop()

    # Schritt 4: Altersverifikation ausfuellen
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()

    # 🎯 DER EXPLICIT WAIT (الانتظار المشروط الذكي):
    # نأمروا السيلينيوم يصبر لغاية ما يافطة "You are underage" تختفي وتطير تماماً من الشاشة قبل ما يرص على التفاح
    underage_toast = (By.XPATH, "//*[contains(text(), 'You are underage') or contains(@class, 'toast')]")
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(underage_toast))

    # Schritt 5: Produkte in den Warenkorb legen
    shipping_page = ShippingPage(browser)
    shipping_page.enter_apples_quantity("5")

    # Schritt 6: Add to Cart via JS-Click ausfuehren, um Overlays zu umgehen
    add_btn = browser.find_element(By.XPATH,
                                   "//div[contains(., 'Gala Apples')]/following-sibling::div//button[contains(., 'Add to Cart')]")
    browser.execute_script("arguments[0].click();", add_btn)


    # Schritt 7: Warenkorb oeffnen und Verifikation
    shipping_page.go_to_checkout()

    # 4.95€ Check laut Spezifikation
    assert "4.95" not in browser.page_source
