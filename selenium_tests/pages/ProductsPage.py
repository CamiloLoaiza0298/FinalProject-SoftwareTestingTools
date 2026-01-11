from selenium.webdriver.common.by import By
import time

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    SEARCH_BOX = (By.ID, "search-input")

    # Methods
    def enter_search_text(self, text):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(text)

    def is_product_found(self):
        try:
            self.driver.find_element(By.XPATH, "//*[@id='products']/div/div")
            return True
        except:
            return False

    def add_to_cart(self):
        product_add_button = self.driver.find_element(By.XPATH, f"//*[@id='products']/div/div/button[2]")
        product_add_button.click()
        time.sleep(1)  # Wait to observe the action

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)  # Wait to observe the action