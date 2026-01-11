from pages.HomePage import HomePage
from pages.ProductsPage import ProductsPage
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
import os
import pytest
import time

class TestE2E:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/index.html'))
        self.driver.get(f"file://{file_path}")

    @pytest.mark.parametrize("username,password,text,fullname,email,address,city,postalcode,cardholder,cardnumber,expiry,cvv,expected", [
        ("testuser1", "password123", "Pot", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "valid"),
        ("testuser1", "password123", "Lamp", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "invalid search"),
        ("wronguser", "password123", "Pot", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "invalid login"),
    ])

    def test_login_and_navigate(self, username, password, text, fullname, email, address, city, postalcode, cardholder, cardnumber, expiry, cvv, expected):
        home_page = HomePage(self.driver)
        
        # Navigate to Login Page
        home_page.click_login_link()
        
        # Perform Login
        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        if expected == "invalid login":
            assert "login" in self.driver.current_url, "Expected to remain on login page for invalid credentials"
        else:
        
        # Navigate to Products Page
            home_page.click_products_link()

            products_page = ProductsPage(self.driver)
            products_page.enter_search_text(text)
            time.sleep(2)  # Wait to observe the search action

            if expected == "invalid search":
                assert not products_page.is_product_found(), "Expected no products for invalid search"
            else:
                products_page.add_to_cart()

                products_page.accept_alert()
                
                # Navigate to Cart Page
                home_page.click_cart_link()

                shop_page = ShopPage(self.driver)
                shop_page.click_checkout()

                # Fill in checkout details
                shop_page.fill_checkout_details(
                    fullname, email, address, city, postalcode, cardholder, cardnumber, expiry, cvv
                )

                shop_page.click_place_order()

                # Verify success message
                success_message = shop_page.get_success_message()
                assert "Thank you! Your order has been placed." in success_message
