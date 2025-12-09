from selenium.webdriver.common.by import By
       
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    SHOW_PASS = (By.CLASS_NAME, "show-pass")
    MESSAGE = (By.ID, "login-msg")

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        
    def toggle_pass_visibility(self):
        self.driver.find_element(*self.SHOW_PASS).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE).text