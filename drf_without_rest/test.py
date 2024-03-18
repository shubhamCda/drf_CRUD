import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

# EmployeeDataCBV

# Apllication Level Exception Handling

# def get_resp(id):
#     response = requests.get(BASE_URL+ENDPOINT+id)
#     # if response.status_code in range(200,300): //OR//
#     if response.status_code == requests.codes.ok:   # Using requests module's 'ok' attribute to check for status code 200
#         print(response.json())
#     else:
#         print("Error with status code", response.status_code)
#     # print(response.status_code)
#     # print(response.json())

# # id = input("Enter some id: ")
# # get_resp(id=id) # Get all

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

# get_all()
# get_resp('11')
# get_all()  # To call all the entries from database --> drf_without_rest> py manage.py dumpdata api.Employee
            # py manage.py dumpdata api.Employee --indent 4 to arrange
            # py manage.py dumpdata api.Employee --format json --indent 4 --> ame as above (default:JSON format)

def create_resource():
    new_emp = {
        'eno': 600,
        'ename':'Jane Doe',
        'esal': 40000,
        'eaddr':'New Orleans'
    }
    # json_data = json.dumps(new_emp)   # Converts Python object into JSON String format
    res = requests.post(BASE_URL + ENDPOINT, json=new_emp)
    print(res.status_code)
    print(res.json())

create_resource()