from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        #  Locators
        self.profile_icon = (By.XPATH, "//div[@class='headerIcon']")

        self.username_input = (By.XPATH, "//input[@type='email']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button_element = (By.XPATH, "//button[@type='submit']")

    def click_profile(self):
        self.driver.find_element(*self.profile_icon).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def login_buton(self):
        self.driver.find_element(*self.login_button_element).click()

    def enter_shop(self):
        shop_btn = (By.XPATH, "//button[contains(text(), 'Shop') or contains(text(), 'SHOP')]")
        self.driver.find_element(*shop_btn).click()
