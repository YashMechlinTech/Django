import requests
import json

# endpoint="https://www.httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"
response = requests.get(
    endpoint, params={"abc": 123, "id": 45}, json={"query": "Hello world!"},
)
print(response)  # Application programming interface

# print(response.text)


# Http request ->http response
# rest api response ->json response


# javascript object notation ~ Python dictionary


print(response.json())
print(response.status_code)
