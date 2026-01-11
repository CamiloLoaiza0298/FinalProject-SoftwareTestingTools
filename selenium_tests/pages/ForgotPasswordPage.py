from selenium.webdriver.common.by import By
import time

class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME = (By.ID, "username")
    CODE = (By.ID, "code")
    PASSWORD = (By.ID, "new-password")
    CONFIRM_PASSWORD = (By.ID, "confirm-new-password")
    TOGGLE_PASSWORD = (By.ID, "toggle-pass")
    RESET_BTN = (By.ID, "login-btn")

    # Methods
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_code(self, code):
        self.driver.find_element(*self.CODE).send_keys(code)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_reset(self):
        self.driver.find_element(*self.RESET_BTN).click()

    def reset(self, username, code, password, confirm_password):
        self.enter_username(username)
        self.enter_code(code)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_reset()
        #explicit wait to ensure page loads after login
        time.sleep(2)
