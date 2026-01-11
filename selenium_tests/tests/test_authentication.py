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
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/login.html'))
    driver.get(f"file://{file_path}")

    
    login = LoginPage(driver)
    login.login(username, password)

    if expected == "valid":
        assert "index" in driver.current_url
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
        assert "login" in driver.current_url
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