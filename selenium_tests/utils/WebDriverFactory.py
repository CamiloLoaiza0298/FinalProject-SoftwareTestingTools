#----------------------------------------------------- 
#Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
#Written by: Juan Camilo Loaiza Alarcon - 6805001
#This project is a software testing suite for a web application; using HTML, CSS and JavaScript for the webpage, and selenium and katalon for automated testing.
#-----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class WebDriverFactory:

    def __init__(self, browser):
        # Set up with the chosen browser
        self.browser = browser

    def get_driver(self):
        # Return the appropriate WebDriver instance
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
