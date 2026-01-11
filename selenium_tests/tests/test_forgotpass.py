from pages.ForgotPasswordPage import ForgotPasswordPage
import os
import csv
import pytest

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'resetpass.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append((row['username'], row['code'], row['password'], row['confirm_password'], row['expected']))

@pytest.mark.parametrize("username,code,password,confirm_password,expected", test_data)
def test_reset_password(driver, username, code, password, confirm_password, expected):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/forgot-password.html'))
    driver.get(f"file://{file_path}")

    register = ForgotPasswordPage(driver)
    register.reset(username, code, password, confirm_password)
    if expected == "valid":
        assert "login" in driver.current_url
    else:
        assert "forgot-password" in driver.current_url