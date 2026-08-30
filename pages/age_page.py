from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AgePage:
    def __init__(self, driver):
        self.driver = driver

        # --- قجر العناوين (Die Locators الحقيقية المضمونة) ---
        self.age_input = (By.XPATH, "//div[contains(@class, 'modal')]//input | //input[@placeholder='DD-mm-YYYY']")

        self.confirm_button = (By.XPATH, "//button[text()='Confirm']")

    # --- قجر الحركات (Die Actions المحمية بالـ Wait الذكي) ---
    def enter_birthdate(self, date_str):
        # اصبر لغاية ما الخانة تظهر وتكون واطية وجاهزة للكتابة (حد أقصى 10 ثواني)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.age_input)
        )
        element.click()  # رص كليك عليها الأول
        element.clear()  # نظف الخانة
        element.send_keys(str(date_str))  # اكتب التاريخ صريح كـ String

    def click_confirm(self):
        # اصبر لغاية ما زر الـ Confirm يظهر ويكون قابل للرص
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_button)
        )
        button.click()
