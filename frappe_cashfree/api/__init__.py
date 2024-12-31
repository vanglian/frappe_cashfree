import frappe
from frappe.utils.password import get_decrypted_password

def authenticate():
    '''Authenticate with CashFree API'''
    
    cashfree_settings = frappe.get_doc("CashFree Settings")
    if not cashfree_settings:
        frappe.throw("CashFree Settings not found")
    
    AppID = cashfree_settings.appid
    if not AppID:
        frappe.throw("AppID is missing in CashFree Settings")
    
    secret_key = get_decrypted_password('CashFree Settings', cashfree_settings.name, 'secret_key')
    if not secret_key:
        frappe.throw("Secret Key is missing in CashFree Settings")
    
    base_url = cashfree_settings.base_url
    if not base_url:
        frappe.throw("Base URL is missing in CashFree Settings")
    
    # Debug prints
    # print(f"AppID: {AppID}")
    # print(f"Secret Key: {secret_key}")
    # print(f"Base URL: {base_url}")
    
    return AppID, secret_key, base_url

# Function to return the Environment setting
@frappe.whitelist(allow_guest=True)
def get_environment():
    '''Get the Environment setting'''
    
    cashfree_settings = frappe.get_doc("CashFree Settings")
    if not cashfree_settings:
        frappe.throw("CashFree Settings not found")
    
    environment = cashfree_settings.environment
    if not environment:
        frappe.throw("Environment is missing in CashFree Settings")
    
    return environment
