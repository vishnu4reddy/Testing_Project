from Libraries.github import LoginPage
from playwright.sync_api import Page
from Data import config
Email = config.user_git
password = config.git_pass


def test_check_login(page: Page):

    login_page = LoginPage(page)
    login_page.navigate()
