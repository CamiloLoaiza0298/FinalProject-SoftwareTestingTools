from pages.RegisterPage import RegisterPage
import os
import csv
import pytest

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'registration.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append((row['username'], row['email'], row['age'], row['password'], row['confirm_password'], row['expected']))

@pytest.mark.parametrize("username,email,age,password,confirm_password,expected", test_data)
def test_valid_registration(driver, username, email, age, password, confirm_password, expected):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/register.html'))
    driver.get(f"file://{file_path}")

    register = RegisterPage(driver)
    register.register(username, email, age, password, confirm_password)
    if expected == "valid":
        assert "created" in driver.current_url
    else:
        assert "register" in driver.current_url
