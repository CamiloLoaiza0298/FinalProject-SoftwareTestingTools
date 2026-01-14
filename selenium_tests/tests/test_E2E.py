#----------------------------------------------------- 
#Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
#Written by: Juan Camilo Loaiza Alarcon - 6805001
#This project is a software testing suite for a web application; using HTML, CSS and JavaScript for the webpage, and selenium and katalon for automated testing.
#-----------------------------------------------------

from pages.HomePage import HomePage
from pages.ProductsPage import ProductsPage
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
import os
import pytest
import time
from utils.ExcelUtility import add_result

class TestE2E:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # Open the homepage before each test
        self.driver = driver
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/index.html'))
        self.driver.get(f"file://{file_path}")

    # Test different login and purchase scenarios
    @pytest.mark.parametrize("username,password,text,fullname,email,address,city,postalcode,cardholder,cardnumber,expiry,cvv,expected,testcase_id", [
        ("testuser1", "password123", "Pot", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "valid", 1),
        ("testuser1", "password123", "Lamp", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "invalid search", 2),
        ("wronguser", "password123", "Figurine", "Juan Camilo Loaiza Alarcon", "jcloaizaa@example.com", "123 Av. Example", "Montreal", "12345", "Juan Camilo Loaiza Alarcon", "12345678910111213", "12/25", "123", "invalid login", 3),
    ])

    def test_login_and_navigate(self, username, password, text, fullname, email, address, city, postalcode, cardholder, cardnumber, expiry, cvv, expected, testcase_id):
        # Start from the home page
        home_page = HomePage(self.driver)
        
        # Go to login page
        home_page.click_login_link()
        
        # Try to log in
        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        if expected == "invalid login":
            # Should stay on login page if login fails
            assert "login" in self.driver.current_url, "Expected to remain on login page for invalid credentials"
            add_result(
                scenario="Test E2E",
                test_id=f"TCE00{testcase_id}",
                description="Invalid login attempt during E2E test",
                steps="""1. Navigate to home page
2. Click login link
3. Enter username and password
4. Click login button
5. Verify redirection to home page""",
                expected=expected,
                actual="Invalid",
                status="Pass",
                testdata=f"Username: {username}, Password: {password}"
            )
        else:
        
        # Navigate to Products Page
            home_page.click_products_link()

            products_page = ProductsPage(self.driver)
            products_page.enter_search_text(text)
            time.sleep(2)  # Wait to observe the search action

            if expected == "invalid search":
                # Should not find product if search is invalid
                assert not products_page.is_product_found(), "Expected no products for invalid search"
                add_result(
                    scenario="Test E2E",
                    test_id=f"TCE00{testcase_id}",
                    description="Invalid product search during E2E test",
                    steps="""1. Navigate to home page
2. Click login link
3. Enter username and password
4. Click login button
5. Verify redirection to home page
6. Navigate to products page
7. Enter search text
8. Verify if products are found""",
                    expected=expected,
                    actual="Invalid",
                    status="Pass",
                    testdata=f"Username: {username}, Password: {password}, Search Text: {text}"
                )
            else:
                # Add product to cart and checkout
                products_page.add_to_cart()
                products_page.accept_alert()
                # Go to cart
                home_page.click_cart_link()

                shop_page = ShopPage(self.driver)
                shop_page.click_checkout()

                # Fill out checkout form
                shop_page.fill_checkout_details(
                    fullname, email, address, city, postalcode, cardholder, cardnumber, expiry, cvv
                )

                shop_page.click_place_order()

                # Verify success message
                success_message = shop_page.get_success_message()
                assert "Thank you! Your order has been placed." in success_message
                add_result(
                    scenario="Test E2E",
                    test_id=f"TCE00{testcase_id}",
                    description="Complete E2E test with valid data",
                    steps="""1. Navigate to home page
2. Click login link
3. Enter username and password
4. Click login button
5. Verify redirection to home page
6. Navigate to products page
7. Enter search text
8. Verify if products are found
9. Add product to cart
10. Accept alert
11. Navigate to cart page
12. Click checkout
13. Fill in checkout details
14. Click place order
15. Verify success message""",
                    expected=expected,
                    actual="Valid",
                    status="Pass",
                    testdata=f"Username: {username}, Password: {password}, Search Text: {text}, Fullname: {fullname}, Email: {email}, Address: {address}, City: {city}, Postalcode: {postalcode}, Cardholder: {cardholder}, Cardnumber: {cardnumber}, Expiry: {expiry}, CVV: {cvv}"
                )
