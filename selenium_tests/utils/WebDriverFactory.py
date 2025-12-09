from selenium import webdriver

class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        if self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            return webdriver.Firefox()
        else:
            raise Exception("Browser not supported")
