
from pages.login_page import LoginPage
from pages.shipping_page import ShippingPage
from pages.age_page import AgePage
from utils import constants
from pages.shop_page import ShopPage


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


    # Schritt 3: Shop oeffnen
    shop_page = ShopPage(browser)
    shop_page.enter_shop()



    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()
    shipping_page = ShippingPage(browser)

    # 1. إدخال الكمية "5" بالماكينة الجاهزة للمطور
    shipping_page.enter_apples_quantity("5")

    # 2. قنص زر الـ Add to Cart بالـ XPath المباشر عشان نتفادوا أي حجب
    add_btn = browser.find_element("xpath",
                                   "//div[contains(., 'Gala Apples')]/following-sibling::div//button[contains(., 'Add to Cart')]")
    browser.execute_script("arguments.click();", add_btn)

    # 3. 🚀 الحل الصَح: اضغط على أيقونة السلة الفوقية (Cart Icon) عشان تفتح صفحة الحسبة
    shipping_page.click_cart_icon()

    # 4. الميزان والتأكد من البق تاعت الـ 4.95 يورو
    assert "4.95" not in browser.page_source
