import requests


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = 'apijsoncbv/'

# response = requests.get(BASE_URL+ENDPOINT)
# response = requests.post(BASE_URL+ENDPOINT)
# response = requests.put(BASE_URL+ENDPOINT)
response = requests.delete(BASE_URL+ENDPOINT)


# Testing the /api/ endpoint
data = response.json()

print('Data from django application: ')
# print('Emp Number: ', data['eno'])
# print('Emp Name: ', data['ename'])
# print('Emp Salary: ', data['esal'])
# print('Emp Address: ', data['eaddr'])

print("<>"*50)
print(data)
print(response.text)