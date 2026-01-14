#----------------------------------------------------- 
#Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
#Written by: Juan Camilo Loaiza Alarcon - 6805001
#This project is a software testing suite for a web application; using HTML, CSS and JavaScript for the webpage, and selenium and katalon for automated testing.
#-----------------------------------------------------

from pages.LoginPage import LoginPage
import os
import csv
import pytest
from utils.ExcelUtility import add_result

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'credentials.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    testcase_id = 0
    for row in reader:
        testcase_id += 1
        test_data.append((row['username'], row['password'], row['expected'], row['comment'], testcase_id))

@pytest.mark.parametrize("username,password,expected,comment,testcase_id", test_data)
def test_valid_login(driver, username, password, expected, comment, testcase_id):
    # Open login page and try to log in
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/login.html'))
    driver.get(f"file://{file_path}")

    
    login = LoginPage(driver)
    login.login(username, password)

    # Check if login is valid or invalid
    if expected == "valid":
        assert "index" in driver.current_url  # Should redirect to home page
        # Record result in Excel
        add_result(
            scenario="Login Test",
            test_id=f"TCA00{testcase_id}",
            description=comment,
            steps="""1. Navigate to login page
2. Enter username and password
3. Click login button
4. Verify redirection to home page""",
            expected=expected,
            actual="Valid",
            status="Pass",
            testdata=f"Username: {username}, Password: {password}"
        )
    else:
        assert "login" in driver.current_url  # Should stay on login page
        # Record result in Excel
        add_result(
            scenario="Login Test",
            test_id=f"TCA00{testcase_id}",
            description=comment,
            steps="""1. Navigate to login page
2. Enter username and password
3. Click login button
4. Verify redirection to home page""",
            expected=expected,
            actual="Invalid",
            status="Pass",
            testdata=f"Username: {username}, Password: {password}"
        )