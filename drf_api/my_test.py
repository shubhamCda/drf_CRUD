import requests


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = 'apijson'

response = requests.get(BASE_URL+ENDPOINT)


# Testing the /api/ endpoint
print(response.json())
