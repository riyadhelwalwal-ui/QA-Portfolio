from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # حد أمان مرن وقوي جداً (15 ثانية) موحد للملف بالكامل
        self.wait = WebDriverWait(self.driver, 15)

        # Locators الأصلية المستقرة بتاعك بعد تصليح إكس بات البروفايل الشرعي
        self.profile_icon = (By.XPATH, "(//div[@class='headerIcon'])[1]")
        self.username_input = (By.XPATH, "//input[@type='email']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button_element = (By.XPATH, "//button[@type='submit']")

    def click_profile(self):
        # انتظار وجود الأيقونة أولاً ثم الضغط بنظافة
        element = self.wait.until(EC.presence_of_element_located(self.profile_icon))
        element.click()

    def enter_username(self, username):
        # انتظار وجود مربع النص لغاية ما تفتح الواجهة
        element = self.wait.until(EC.presence_of_element_located(self.username_input))
        element.send_keys(username)

    def enter_password(self, password):
        # كتابة مباشرة بدون انتظار زايد لزيادة سرعة التست
        self.driver.find_element(*self.password_input).send_keys(password)

    def login_buton(self):
        # ضغط مباشر بدون انتظار زايد
        self.driver.find_element(*self.login_button_element).click()

    def enter_shop(self):
        # الـ XPath الشرعي المظبوط امتاع الـ <a> اللي صيدته بيدك وعينك السينيور
        shop_link = (By.XPATH, "//a[contains(text(), 'Shop') or contains(text(), 'SHOP')]")

        # الانتظار الذكي الكلاسيكي الصافي: راجي لغاية ما الرابط يقعد قابل للضغط واكبس طول بنظافة
        self.wait.until(EC.element_to_be_clickable(shop_link)).click()

    def wait_until_login_completes(self):
        # راجي لغاية ما كلمة /auth تطير تماماً من الرابط بعد نجاح الدخول
        self.wait.until_not(EC.url_contains("/auth"))
