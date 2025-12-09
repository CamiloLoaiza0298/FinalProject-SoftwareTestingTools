from pages.LoginPage import LoginPage

def test_valid_login(driver):
    # Go to the login page
    driver.get("file:///C:/Users/6805001/Desktop/Camilo/Project/FinalProject-SoftwareTestingTools/website/login.html")
    
    login_page = LoginPage(driver)

    # Perform login
    login_page.login("testuser1", "password123")

    # Assertion: "successful" in ID = login-msg
    message = login_page.get_error_message()
    assert "successful" in message
    
def test_valid_user_invalid_password_login(driver):
    # Go to the login page
    driver.get("file:///C:/Users/6805001/Desktop/Camilo/Project/FinalProject-SoftwareTestingTools/website/login.html")
    
    login_page = LoginPage(driver)

    # Perform login with invalid credentials
    login_page.login("testuser1", "wrongpassword")

    # Assertion: "Invalid username or password" in ID = login-msg
    message = login_page.get_error_message()
    assert "Invalid username or password" in message