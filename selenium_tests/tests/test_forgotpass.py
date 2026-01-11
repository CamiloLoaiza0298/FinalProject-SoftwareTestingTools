from pages.ForgotPasswordPage import ForgotPasswordPage
import os
import csv
import pytest
from utils.ExcelUtility import add_result

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'resetpass.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    testcase_id = 0
    for row in reader:
        testcase_id += 1
        test_data.append((row['username'], row['code'], row['password'], row['confirm_password'], row['expected'], row['comment'], testcase_id))

@pytest.mark.parametrize("username,code,password,confirm_password,expected,comment,testcase_id", test_data)
def test_reset_password(driver, username, code, password, confirm_password, expected, comment, testcase_id):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/forgot-password.html'))
    driver.get(f"file://{file_path}")

    register = ForgotPasswordPage(driver)
    register.reset(username, code, password, confirm_password)
    if expected == "valid":
        assert "login" in driver.current_url
        add_result(
                    scenario="Test Reset Password",
                    test_id=f"TCR00{testcase_id}",
                    description=comment,
                    steps="""1. Navigate to forgot password page
2. Enter username, code, new password, and confirm password
3. Click reset password button
4. Verify redirection to login page""",
                    expected=expected,
                    actual="Valid",
                    status="Pass",
                    testdata=f"Username: {username}, Code: {code}, Password: {password}, Confirm Password: {confirm_password}"
                )
    else:
        assert "forgot-password" in driver.current_url
        add_result(
                    scenario="Test Reset Password",
                    test_id=f"TCR00{testcase_id}",
                    description="Complete E2E test with valid data",
                    steps="""1. Navigate to forgot password page
2. Enter username, code, new password, and confirm password
3. Click reset password button
4. Verify redirection to login page""",
                    expected=expected,
                    actual="Invalid",
                    status="Pass",
                    testdata=f"Username: {username}, Code: {code}, Password: {password}, Confirm Password: {confirm_password}"
                )