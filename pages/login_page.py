from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object Model for Login page"""

    def __init__(self, page: Page):
        self.page = page
        self.input_name = page.locator("[name='username']")
        self.input_password = page.locator("[name='password']")
        self.login_button = page.locator("#btnLogin")

    def navigate(self):
        self.page.goto("")

    def login(self, username, password):
        self.input_name.fill(username)
        self.input_password.fill(password)
        self.login_button.click()
