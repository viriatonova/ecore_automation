import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.test_data import TestData


@pytest.mark.e2e
def test_successful_login(page: Page, login_page: LoginPage):
    login_page.navigate()
    login_page.login(TestData.valid_username, TestData.valid_password)
    expect(page).to_have_url(re.compile(r"/account"))
    expect(page.locator(TestData.invoice_list_locator)).to_be_visible()


@pytest.mark.e2e
@pytest.mark.parametrize(
    ["username", "password"],
    [
        ("", ""),
        ("Demouser", "abc123"),
        ("demouser_", "xyz"),
        ("demouser", "nananana"),
        ("demouser", "abc123"),
    ],
)
def test_failed_login(username, password, page: Page, login_page: LoginPage):
    login_page.navigate()
    login_page.login(username, password)
    expect(page.locator(TestData.error_message_locator)).to_be_visible()
