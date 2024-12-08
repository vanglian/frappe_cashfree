import frappe
import requests
import json
from frappe_cashfree.api import authenticate

AppID, secret_key, base_url = authenticate()

headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'x-api-version': '2023-08-01',
  'x-client-id': AppID,
  'x-client-secret': secret_key
}

@frappe.whitelist(allow_guest=True)
def create_order(**kwargs):
    # Ensure mandatory fields are provided
    mandatory_fields = ["order_amount", "order_currency", "customer_id", "customer_name", "customer_phone"]
    for field in mandatory_fields:
        if field not in kwargs or kwargs[field] is None:
            return {"status": "error", "message": f"Missing mandatory field {field}"}

    url = f"{base_url}/pg/orders"
    payload = json.dumps({
        "customer_details": {
            "customer_id": kwargs["customer_id"],
            "customer_phone": kwargs["customer_phone"],
            "customer_email": kwargs.get("customer_email"),
            "customer_name": kwargs["customer_name"]
        },
        "order_id": kwargs.get("order_id"),
        "order_currency": kwargs["order_currency"],
        "order_amount": kwargs["order_amount"]
        "order_meta":{
            "return_url": kwargs.get("return_url"),
        }
    })
    
    # Debug prints
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")
    
    try:
        api_response = requests.request("POST", url, headers=headers, data=payload)
        print(f"Response Status Code: {api_response.status_code}")
        print(f"Response Text: {api_response.text}")
        return {"status_code": api_response.status_code, "response": api_response.json()}
    except requests.exceptions.HTTPError as http_err:
        frappe.log_error(f"HTTP error occurred: {http_err}")
        return {"status_code": api_response.status_code, "error": str(http_err)}
    except Exception as e:
        frappe.log_error(f"An error occurred: {e}")
        return {"status_code": 500, "error": str(e)}