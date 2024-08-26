import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name': 'Rahul',
    'roll': '101',
    'city': 'Ranchi'
}

# Convert Python dictionary to JSON string
json_data = json.dumps(data)

# Send POST request with JSON data and proper headers
try:
    r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
    r.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

    # Print the raw response content for debugging
    print("Raw response content:", r.text)

    # Try to parse JSON response
    data = r.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except ValueError as e:
    print(f"Failed to parse JSON: {e}")
