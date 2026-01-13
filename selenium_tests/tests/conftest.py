import pytest
import os
from utils.WebDriverFactory import WebDriverFactory
from utils.ExcelUtility import write_results_to_excel

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

@pytest.fixture(scope="session", autouse=True)
def export_results_after_tests():
    # Run tests
    yield
    # Runs once after all tests finish
    write_results_to_excel()
