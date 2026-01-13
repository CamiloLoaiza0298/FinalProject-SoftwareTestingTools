from pages.HomePage import HomePage
import os
import csv
from utils.ExcelUtility import add_result
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

    home.interact_with_video(driver)

    # Switch back to default content
    home.switch_to_default_content()

    # Click on another element to verify we are back to default content
    home.click_products_link()

    add_result(
            scenario="Login Test",
            test_id=f"TCI001",
            description="Interact with video inside iframe",
            steps="""1. Navigate to home page
2. Switch to iframe containing video
3. Click play button on video
4. Switch back to default content
5. Click on Products link""",
            expected="valid",
            actual="valid",
            status="Pass",
            testdata="N/A"
        )