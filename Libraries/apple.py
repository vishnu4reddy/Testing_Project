from playwright.sync_api import Page
from Data.cred import email, password


class AppTesting:
    def __init__(self, page: Page):
        """
        Initialize the AppTesting class.

        Args:
            page (Page): The Playwright Page object to interact with the web page.
        """
        self.page = page
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.apple_sign_in_button = page.frame_locator(
            "iframe[name=\"aid-auth-widget\"]").get_by_label("Sign In with your Apple ID")
        self.apple_continue = page.frame_locator(
            "iframe[name=\"aid-auth-widget\"]").get_by_label("Continue")
        self.apple_sign_in_button_pass = page.frame_locator(
            "iframe[name=\"aid-auth-widget\"]").get_by_label("Password").fill(password)

    def navigate_to_icloud(self):
        """
        Navigate to the iCloud website.
        """

        self.page.goto("https://www.icloud.com/")

    def click_sign_in(self):
        """
        Click the 'Sign In' button on the web page.
        """

        self.sign_in_button.click()

    def login_with_apple_id(self):
        """
        Perform the login with the provided Apple ID.

        Args:
            email_address (str): The email address associated with the Apple ID.
        """

        self.apple_sign_in_button.click()
        self.apple_sign_in_button.fill(email)
        self.apple_sign_in_button_pass.click()
        self.apple_continue.click()
        # self.apple_sign_in_button_pass.fill(password)

    # page.get_by_role("button", name="Sign In").click()
    # page.frame_locator("iframe[name=\"aid-auth-widget\"]").get_by_label("Sign In with your Apple ID").click()
    # page.frame_locator("iframe[name=\"aid-auth-widget\"]").get_by_label("Sign In with your Apple ID").fill("vishnuvardhanuv36@gmail.com")
    # page.frame_locator("iframe[name=\"aid-auth-widget\"]").get_by_label("Continue").click()
    # page.frame_locator("iframe[name=\"aid-auth-widget\"]").get_by_label("Password").fill("Chandra@12")
    # page.frame_locator("iframe[name=\"aid-auth-widget\"]").get_by_label("Sign In", exact=True).click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class YourTestClass:
#     def __init__(self):

#         driver = webdriver.Chrome()  # Change to the appropriate driver for your browser

#         # Navigate to the desired page
#         driver.get("your_page_url_here")

#         # Assign elements to instance variables
#         self.sign_in = selfdriver.find_element(By.CSS_SELECTOR, "button[name='Sign In']")
#         self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[name='aid-auth-widget']"))
#         self.apple_sign_in = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In with your Apple ID')]")

# # Create an instance of your class and use the elements as needed
# your_instance = YourTestClass()
# your_instance.sign_in.click()
# your_instance.apple_sign_in.click()
