import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resp(url):
    response = requests.get(BASE_URL+ENDPOINT)
    print(response.status_code)
    print(response.json())

get_resp(url=BASE_URL+"users/") # Get all
