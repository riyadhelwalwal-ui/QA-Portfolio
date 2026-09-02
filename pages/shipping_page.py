from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingPage:
    def __init__(self, driver):
        self.driver = driver
        # حد أمان مرن وقوي جداً (15 ثانية) موحد للملف بالكامل
        self.wait = WebDriverWait(self.driver, 15)

        # --- Element-Lokatoren (Gala Apples & Cart) ---
        self.apples_qty = (By.XPATH, "//div[contains(., 'Gala Apples')]/following-sibling::div//input[@type='number']")
        self.add_to_cart_btn = (By.XPATH,
                                "//div[contains(., 'Gala Apples')]/following-sibling::div//button[contains(text(), 'Add to Cart')]")
        self.cart_icon = (By.XPATH, "(//div[@class='headerIcon'][3])")

        # --- Lokatoren für das Checkout-Formular und Kauf ---
        self.street_name = (By.XPATH, "//input[@placeholder='Street Address']")
        self.city_name = (By.XPATH, "//input[@placeholder='City']")
        self.post_code = (By.XPATH, "//input[@placeholder='Postal Code']")
        self.card_number = (By.XPATH, "//input[@placeholder='Card number']")
        self.name_on_card = (By.XPATH, "//input[@placeholder='Name on card']")
        self.expiration = (By.XPATH, "//input[@placeholder='Expiration']")
        self.cvv = (By.XPATH, "//input[@placeholder='Cvv']")
        self.buy_btn = (By.XPATH, "//button[@class='btn-buy-now']")

    # --- Seiten-Aktionen ---
    def enter_apples_quantity(self, number_to_add):
        element = self.wait.until(EC.element_to_be_clickable(self.apples_qty))
        element.click()
        element.send_keys(str(number_to_add))

    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()

    def go_to_checkout(self):
        # 🎯 الدالة المنقذة اللي كانت ناقصة ومسببة الكراش
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def fill_checkout_and_buy(self):
        # استدعاء ملف التوابت لداخل الدالة بنظافة تامة
        from utils import constants

        # 1. تعبئة بيانات العنوان والشحن المسحوبة من باج التوابت بالملي
        self.wait.until(EC.presence_of_element_located(self.street_name)).send_keys(constants.SHIPPING_ADDRESS)
        self.driver.find_element(*self.city_name).send_keys(constants.CITY)
        self.driver.find_element(*self.post_code).send_keys(constants.POST_CODE)

        # 2. تعبئة بيانات الكرت الحساسة المسحوبة من باج التوابت بالملي
        self.driver.find_element(*self.card_number).send_keys(constants.FAKE_CARD)
        self.driver.find_element(*self.name_on_card).send_keys(constants.FIRST_NAME + " " + constants.LAST_NAME)
        self.driver.find_element(*self.expiration).send_keys(constants.EXPIRATION_DATE)
        self.driver.find_element(*self.cvv).send_keys(constants.FAKE_CVV)

        # 3. الضغط العسكري على زر الشراء النهائي المظبوط
        self.wait.until(EC.element_to_be_clickable(self.buy_btn)).click()
