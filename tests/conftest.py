import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def invoice_page(page: Page) -> InvoicePage:
    return InvoicePage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Fixture to provide a LoginPage instance for tests."""
    """Fixture to set browser context arguments"""
    return {
        **browser_context_args,
        "base_url": "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/",
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "ignore_https_errors": True,
    }
