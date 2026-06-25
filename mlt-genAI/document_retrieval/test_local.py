import json
from app import lambda_handler

# Mock the API Gateway event
mock_event = {
    "body": json.dumps({
        "ticker": "AAPL",
        "year": "2024",
        "form_type": "Q1"
    })
}

# Call the handler directly
response = lambda_handler(mock_event, None)
print(response)