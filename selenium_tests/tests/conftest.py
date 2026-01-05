import pytest
from utils.WebDriverFactory import WebDriverFactory

@pytest.fixture()
def driver():
    factory = WebDriverFactory("firefox")
    driver = factory.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
