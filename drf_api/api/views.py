from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


# Create your views here.
def emp_data_view(request):
    EmpData = {"eno": 101, "ename": "Shubh", "esal": 10000, "eaddr": "Nagpur"}

    resp = f"<h1>Emp Number : {EmpData['eno']}<br>Emp Name : {EmpData['ename']}<br>Emp Salary : {EmpData['esal']}<br>Emp Address : {EmpData['eaddr']}<br></h1>"
    return HttpResponse(resp)

def json_data_view(request):
    EmpData = {
        "eno": 102, 
        "ename": "Sandy", 
        "esal": 20000, 
        "eaddr": "Mumbai"
        }
    json_data =  json.dumps(EmpData)
                                                  #MIME type -> multipurpose internet male extensions  
    return HttpResponse(json_data, content_type='application/json')

def json_data_view_02(request):
    EmpData = {
        "eno": 103, 
        "ename": "Rohit", 
        "esal": 30000, 
        "eaddr": "Nashik"
        }
                                                      #MIME type -> multipurpose internet male extensions  
    return JsonResponse(EmpData)

