from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    LOGIN_LINK = (By.CLASS_NAME, "fa-user")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    CART_LINK = (By.CLASS_NAME, "fa-cart-shopping")
    EMBEDDED_VIDEO = (By.CLASS_NAME, "video-container")

    # Methods
    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def click_products_link(self):
        self.driver.find_element(*self.PRODUCTS_LINK).click()

    def click_cart_link(self):
        self.driver.find_element(*self.CART_LINK).click()
