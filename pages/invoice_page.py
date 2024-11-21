from playwright.sync_api import Page, BrowserContext
from pages.login_page import LoginPage
from utils.test_data import TestData


class InvoicePage:
    """Page Object Model for Invoice page"""

    def __init__(self, page: Page):
        self._page = page

    def _autenticate(self):
        self._page.goto("")
        login_page = LoginPage(self._page)
        login_page.login(TestData.valid_username, TestData.valid_password)

    def get_invoice_page(self, hotel_name, context: BrowserContext):
        self._autenticate()
        with context.expect_page() as new_page_info:
            self._page.locator(
                f"//div[contains(text(),'{hotel_name}')]/following-sibling::div/a"
            ).nth(1).click()
        return new_page_info.value
