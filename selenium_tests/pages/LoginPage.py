#----------------------------------------------------- 
#Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
#Written by: Juan Camilo Loaiza Alarcon - 6805001
#This project is a software testing suite for a web application; using HTML, CSS and JavaScript for the webpage, and selenium and katalon for automated testing.
#-----------------------------------------------------

from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")

    # Methods
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        #explicit wait to ensure page loads after login
        time.sleep(2)

