from selenium.webdriver.common.by import By
import time

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    AGE = (By.ID, "age")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm-password")
    TOGGLE_PASSWORD = (By.ID, "toggle-pass")
    LOGIN_BTN = (By.CLASS_NAME, "register-btn")

    # Methods
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_age(self, age):
        self.driver.find_element(*self.AGE).send_keys(age)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def register(self, username, email, age, password, confirm_password):
        self.enter_username(username)
        self.enter_email(email)
        self.enter_age(age)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register()
        #explicit wait to ensure page loads after login
        time.sleep(2)
