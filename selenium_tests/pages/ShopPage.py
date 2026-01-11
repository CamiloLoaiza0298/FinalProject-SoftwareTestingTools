from selenium.webdriver.common.by import By
import time

class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    CHECKOUT_BUTTON = (By.ID, "open-checkout")
    FULLNAME_INPUT = (By.ID, "full-name")
    EMAIL_INPUT = (By.ID, "email")
    ADDRESS_INPUT = (By.ID, "address")
    CITY_INPUT = (By.ID, "city")
    POSTALCODE_INPUT = (By.ID, "postal")
    CARDHOLDER_INPUT = (By.ID, "card-name")
    CARDNUMBER_INPUT = (By.ID, "card-number")
    EXPIRY_INPUT = (By.ID, "expiry")
    CVV_INPUT = (By.ID, "cvv")
    PLACE_ORDER_BUTTON = (By.ID, "place-order")

    # Methods
    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        time.sleep(1)  # Wait to observe the action

    def fill_checkout_details(self, fullname, email, address, city, postalcode, cardholder, cardnumber, expiry, cvv):
        self.driver.find_element(*self.FULLNAME_INPUT).send_keys(fullname)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.POSTALCODE_INPUT).send_keys(postalcode)
        self.driver.find_element(*self.CARDHOLDER_INPUT).send_keys(cardholder)
        self.driver.find_element(*self.CARDNUMBER_INPUT).send_keys(cardnumber)
        self.driver.find_element(*self.EXPIRY_INPUT).send_keys(expiry)
        self.driver.find_element(*self.CVV_INPUT).send_keys(cvv)

    def click_place_order(self):
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()
        time.sleep(1)  # Wait to observe the action

    def get_success_message(self):
        return self.driver.find_element(By.ID, "checkout-msg").text
    