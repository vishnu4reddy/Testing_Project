from Libraries.apple import AppTesting
from playwright.sync_api import Page
import logging
import os


def test_Sign_in(page: Page):
    app_tester = AppTesting(page)
    logging.info("Running test_navigate_to_icloud")
    app_tester.navigate_to_icloud()
    logging.info("navigate_to_icloud completed successfully.")
    logging.info("Running test_click_sign_in")
    app_tester.click_sign_in()
    logging.info("click_sign_in completed successfully.")
    logging.info("Running test_Login_with_apple_id")
    app_tester.login_with_apple_id()
    logging.info("Login_with_apple_id completed successfully.")


# pytest -s --log-cli-level=INFO
