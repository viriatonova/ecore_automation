from playwright.sync_api import Page


class LoginPage:
    """Page Object Model for Login page"""

    def __init__(self, page: Page):
        self._page = page
        self._input_name = page.locator("[name='username']")
        self._input_password = page.locator("[name='password']")
        self._login_button = page.locator("#btnLogin")

    def navigate(self):
        self._page.goto("")

    def login(self, username, password):
        self._input_name.fill(username)
        self._input_password.fill(password)
        self._login_button.click()
