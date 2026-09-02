from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        # حد أمان مرن وقوي جداً (15 ثانية) موحد للملف
        self.wait = WebDriverWait(self.driver, 15)

        # Lokatoren الحصرية لـ واجهة الشوب والسن بالملي
        self.shop_link = self.shop_link = (By.XPATH, "//a[@href='/store' and contains(text(), 'Shop')]")

        self.birthdate_input = (By.XPATH, "//input[@type='date' or @id='birthdate']")
        self.confirm_age_btn = (By.XPATH, "//button[contains(text(), 'Confirm') or contains(text(), 'Bestätigen')]")

    def enter_shop(self):


        # الانتظار الذكي الكلاسيكي لـ رابط الشوب غصب عن عمارة السيرفر
        self.wait.until(EC.element_to_be_clickable(self.shop_link)).click()

    def pass_age_verification(self, birthdate):
        # تعبئة السن وتطيير البوب أب بنظافة تامة
        element = self.wait.until(EC.visibility_of_element_located(self.birthdate_input))
        element.clear()
        element.send_keys(str(birthdate))
        self.wait.until(EC.element_to_be_clickable(self.confirm_age_btn)).click()
