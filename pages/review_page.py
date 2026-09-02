from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReviewPage:
    def __init__(self, driver):
        self.driver = driver
        # حد أمان مرن وقوي جداً (15 ثانية) موحد للملف
        self.wait = WebDriverWait(self.driver, 15)

        # Element-Locators für das Bewertungssystem
        self.gala_apples_link = (By.XPATH, "//img[@alt='Gala Apples']")
        self.review_textarea = (By.XPATH, "//textarea[@placeholder='What is your view?']")
        self.submit_review_btn = (By.XPATH, "//button[contains(text(), 'Send')]")

    def open_gala_product_page(self):
        # في الـ EC: مستحيل نحطوا علامة النجمة (تنزيل كـ Tuple جاف)
        self.wait.until(EC.element_to_be_clickable(self.gala_apples_link)).click()

    def enter_review_text(self, text):
        # في الـ EC: مستحيل نحطوا علامة النجمة (تنزيل كـ Tuple جاف)
        element = self.wait.until(EC.visibility_of_element_located(self.review_textarea))
        element.clear()
        # في الـ find_element: لابد ولابد من علامة النجمة (*) لتفكيك اللوكاتور
        self.driver.find_element(*self.review_textarea).send_keys(str(text))

    def get_text_lange(self):
        # في الـ EC: مستحيل نحطوا علامة النجمة (تنزيل كـ Tuple جاف)
        self.wait.until(EC.presence_of_element_located(self.review_textarea))
        # في الـ find_element: لابد ولابد من علامة النجمة (*) لتفكيك اللوكاتور
        element = self.driver.find_element(*self.review_textarea)
        return len(element.get_attribute("value"))

    def click_submit_review(self):
        # في الـ EC: مستحيل نحطوا علامة النجمة (تنزيل كـ Tuple جاف)
        self.wait.until(EC.element_to_be_clickable(self.submit_review_btn)).click()
