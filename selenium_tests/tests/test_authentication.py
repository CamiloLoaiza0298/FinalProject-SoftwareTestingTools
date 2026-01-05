from pages.LoginPage import LoginPage
import os
import csv
import pytest

# Read test data from CSV
csv_path = os.path.join(os.path.dirname(__file__), 'credentials.csv')
test_data = []
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append((row['username'], row['password'], row['expected']))

@pytest.mark.parametrize("username,password,expected", test_data)
def test_valid_login(driver, username, password, expected):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/login.html'))
    driver.get(f"file://{file_path}")
    
    login = LoginPage(driver)
    login.login(username, password)

    if expected == "valid":
        assert "index" in driver.current_url
    else:
        assert "login" in driver.current_url
