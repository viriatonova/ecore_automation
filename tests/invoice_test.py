from playwright.sync_api import Page, expect
from pages.invoice_page import InvoicePage
from utils.test_data import TestData


def test_check_invoice(page: Page, invoice_page: InvoicePage):
  invoice = invoice_page.get_invoice_page(TestData.hotel_name, page.context)
  expect(invoice.locator("//h2[contains(text(),'Invoice Details')]")).to_be_visible()