#----------------------------------------------------- 
#Assignment: 420-TZ4-GX SOFTWARE TESTING TOOLS
#Written by: Juan Camilo Loaiza Alarcon - 6805001
#This project is a software testing suite for a web application; using HTML, CSS and JavaScript for the webpage, and selenium and katalon for automated testing.
#-----------------------------------------------------

from pages.RegisterPage import RegisterPage
import os
import csv
import pytest
from utils.ExcelUtility import add_result

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'registration.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    testcase_id = 0
    for row in reader:
        testcase_id += 1
        test_data.append((row['username'], row['email'], row['age'], row['password'], row['confirm_password'], row['expected'], row['comment'], testcase_id))

@pytest.mark.parametrize("username,email,age,password,confirm_password,expected,comment,testcase_id", test_data)
def test_valid_registration(driver, username, email, age, password, confirm_password, expected, comment, testcase_id):
    # Open registration page and try to register
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/register.html'))
    driver.get(f"file://{file_path}")

    register = RegisterPage(driver)
    register.register(username, email, age, password, confirm_password)
    # Check if registration is valid or invalid
    if expected == "valid":
        assert "created" in driver.current_url  # Should redirect to created page
        # Record result in Excel
        add_result(
                    scenario="Test Registration",
                    test_id=f"TCREG00{testcase_id}",
                    description=comment,
                    steps="""1. Navigate to registration page
2. Enter username, email, age, password, and confirm password
3. Click register button""",
                    expected=expected,
                    actual="Valid",
                    status="Pass",
                    testdata=f"Username: {username}, Email: {email}, Age: {age}, Password: {password}, Confirm Password: {confirm_password}"
                )
    else:
        assert "register" in driver.current_url  # Should stay on registration page
        # Record result in Excel
        add_result(
                    scenario="Test Registration",
                    test_id=f"TCREG00{testcase_id}",
                    description=comment,
                    steps="""1. Navigate to registration page
2. Enter username, email, age, password, and confirm password
3. Click register button""",
                    expected=expected,
                    actual="Invalid",
                    status="Pass",
                    testdata=f"Username: {username}, Email: {email}, Age: {age}, Password: {password}, Confirm Password: {confirm_password}"
                )
