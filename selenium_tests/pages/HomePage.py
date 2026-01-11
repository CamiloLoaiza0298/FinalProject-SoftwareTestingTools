from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    LOGIN_LINK = (By.CLASS_NAME, "fa-user")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    CART_LINK = (By.CLASS_NAME, "fa-cart-shopping")
    EMBEDDED_VIDEO = (By.ID, "iframe1")

    # Methods
    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def click_products_link(self):
        self.driver.find_element(*self.PRODUCTS_LINK).click()

    def click_cart_link(self):
        self.driver.find_element(*self.CART_LINK).click()

    def switch_to_video_iframe(self):
        iframe = self.driver.find_element(*self.EMBEDDED_VIDEO)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def interact_with_video(self, driver):
        try:
            # The 'Play' or 'Pause' button has a common class/aria-label
            play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".ytp-play-button.ytp-button"))
            )
            play_button.click()
            print("Clicked the play/pause button.")
        except Exception as e:
            print(f"Could not click play button: {e}")

