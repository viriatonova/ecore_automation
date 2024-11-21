import re
import pytest

from playwright.sync_api import Page, expect
from pages.invoice_page import InvoicePage
from utils.test_data import TestData


@pytest.mark.e2e
def test_check_invoice(page: Page, invoice_page: InvoicePage):
    invoice = invoice_page.get_invoice_page(TestData.hotel_name, page.context)
    expect(invoice.locator(TestData.hotel_name_locator)).to_be_visible()
    expect(invoice.locator(TestData.invoice_date_locator)).to_be_visible()
    expect(invoice.locator(TestData.due_date_locator)).to_be_visible()
    expect(invoice.locator(TestData.invoice_date_locator)).to_be_visible()
    expect(invoice.locator(TestData.booking_code_locator)).to_be_visible()
    expect(invoice.locator(TestData.room_locator)).to_be_visible()
    expect(invoice.locator(TestData.total_stay_count_locator)).to_be_visible()
    expect(invoice.locator(TestData.total_stay_amount_locator)).to_be_visible()
    expect(invoice.locator(TestData.check_in_locator)).to_be_visible()
    expect(invoice.locator(TestData.check_out_locator)).to_be_visible()
    expect(invoice.locator(TestData.deposit_nowt_locator)).to_be_visible()
    expect(invoice.locator(TestData.tax_vat_locator)).to_be_visible()
    expect(invoice.locator(TestData.total_amount_locator)).to_be_visible()
    expect(invoice.locator(TestData.deposit_nowt_value_locator)).to_be_visible()
    expect(invoice.locator(TestData.tax_vat_value_locator)).to_be_visible()
    expect(invoice.locator(TestData.total_amount_value_locator)).to_be_visible()
    customer_detail = invoice.locator(TestData.customer_datail_locator)
    expect(customer_detail).to_have_text(re.compile("JOHNY SMITH"))
    expect(customer_detail).to_have_text(re.compile("R2, AVENUE DU MAROC"))
    expect(customer_detail).to_have_text(re.compile("123456"))
