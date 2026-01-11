from pages.HomePage import HomePage
import os
import csv

from selenium.webdriver.common.by import By
import pytest


#Write a test that locates an element inside an iframe, switches context to interact with it, and then switches back to the default content (link to youtube video)
def test_iframe_interaction(driver):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../website/index.html'))
    driver.get(f"file://{file_path}")

    home = HomePage(driver)

    # Switch to iframe
    home.switch_to_video_iframe()

    # Interact with element inside iframe (e.g., play video)

