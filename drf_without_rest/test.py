import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

# EmployeeDataCBV
def get_resp(id): 
    response = requests.get(BASE_URL+ENDPOINT+id)
    print(response.status_code)
    print(response.json())

# id = input("Enter some id: ")
# get_resp(id=id) # Get all

# EmployeeListCBV
def get_all():
    response = requests.get(BASE_URL+ENDPOINT)
    print(response.status_code)
    print(response.json())

get_all()
