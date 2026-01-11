import pytest
import os
from utils.WebDriverFactory import WebDriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser to run tests on: chrome or firefox")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # To choose browser: python -m pytest --browser chrome
    factory = WebDriverFactory(browser)
    driver = factory.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
