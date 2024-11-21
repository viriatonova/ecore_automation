# flake8: noqa
class TestData:
    valid_username = "demouser"
    valid_password = "abc123"
    hotel_name = "Rendezvous Hotel"

    # Login locators
    invoice_list_locator = "//h2[contains(text(), 'Invoice List')]"
    error_message_locator = "//div[contains(text(), 'Wrong username or password.')]"

    # Invoice locators
    hotel_name_locator = "//h4[contains(text(), 'Rendezvous Hotel')]"
    invoice_date_locator = "//span[contains(text(), 'Invoice Date:')]/parent::li[contains(text(), '14/01/2018')]"
    due_date_locator = "//span[contains(text(), 'Due Date:')]/parent::li[contains(text(), '15/01/2018')]"
    invoice_locator = "//h6[contains(text(), 'Invoice #110 details')]"
    booking_code_locator = "//td[contains(text(),'Booking Code')]/following-sibling::td[contains(text(),'0875')]"
    room_locator = "//td[contains(text(),'Room')]/following-sibling::td[contains(text(),'Superior Double')]"
    total_stay_count_locator = "//td[contains(text(),'Total Stay Count')]/following-sibling::td[contains(text(),'1')]"
    total_stay_amount_locator = "//td[contains(text(),'Total Stay Amount')]/following-sibling::td[contains(text(),'$150')]"
    check_in_locator = "//td[contains(text(),'Check-In')]/following-sibling::td[contains(text(),'14/01/2018')]"
    check_out_locator = "//td[contains(text(),'Check-Out')]/following-sibling::td[contains(text(),'15/01/2018')]"
    deposit_nowt_locator = "//thead/tr/td[contains(text(), 'Deposit Now')]"
    tax_vat_locator = "//thead/tr/td[contains(text(), 'Tax&VAT')]"
    total_amount_locator = "//thead/tr/td[contains(text(), 'Total Amount')]"
    deposit_nowt_value_locator = "//tbody/tr/td[contains(text(), 'USD $20.90')]"
    tax_vat_value_locator = "//tbody/tr/td[contains(text(), 'USD $19.00')]"
    total_amount_value_locator = "//tbody/tr/td[contains(text(), 'USD $209.00')]"
    customer_datail_locator = (
        "//h5[contains(text(),'Customer Details')]/following-sibling::div"
    )
