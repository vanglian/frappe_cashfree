import frappe
from frappe.utils.password import get_decrypted_password

def authenticate():
    cashfree_settings = frappe.get_doc("CashFree Settings")
    AppID = cashfree_settings.appid
    secret_key = get_decrypted_password('CashFree Settings', cashfree_settings.name, 'secret_key')
    base_url = cashfree_settings.base_url
    
    # Debug prints
    # print(f"AppID: {AppID}")
    # print(f"Secret Key: {secret_key}")
    # print(f"Base URL: {base_url}")
    
    return AppID, secret_key, base_url

