import requests
import json

URL = 'http://127.0.0.1:8000/'

def get_data():

    r=requests.get(url=URL)
    print(r.json())
    data=r.json()
    return (data)


# def post_data():
#     data = {
#         'name': 'Ravi',
#         'roll': 104,
#         'city': 'Dhanbad'
#     }

#     json_data = json.dumps(data)  # Convert data into JSON format
#     print(json_data)

#     # Specify the content-type as JSON
#     headers = {'Content-Type': 'application/json'}

#     # Send the POST request
#     r = requests.post(url=URL, data=json_data, headers=headers)

#     # Print the status code and raw response content for debugging
#     print("Response Status Code:", r.status_code)
#     print("Raw Response Content:", r.text)

#     # Attempt to parse the JSON response
#     try:
#         response_json = r.json()  # This will raise an error if the response is not valid JSON
#         print("JSON Response:", response_json)
#     except requests.exceptions.JSONDecodeError as e:
#         print("Failed to decode JSON:", e)

# Calling the function
get_data()
