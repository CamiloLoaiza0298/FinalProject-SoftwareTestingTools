from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        if self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            try:
                return webdriver.Firefox()
            except Exception:
                service = Service(executable_path='/usr/bin/geckodriver')
                return webdriver.Firefox(service=service)
        else:
            raise Exception("Browser not supported")
