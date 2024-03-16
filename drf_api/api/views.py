from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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

# CBV
@method_decorator(csrf_exempt, name="dispatch")
class jsonCBV(View):

    def get(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "This is a GET Method JSON Response"})
        return HttpResponse(json_data, content_type="application/json")

    # EmpData = {
    #     "eno": 104,
    #     "ename": "Soham",
    #     "esal": 40000,
    #     "eaddr": "Dadar"
    #     }

    # return JsonResponse(EmpData)

    # *args(Variable length Arguments) ->any no. of arguments can be provide convert into tuple
    # *kwargs(Variable length Key-Word Arguments) -> any keyword argument can be provided and it will convert into dictionary

    def post(self,  request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is a POST Method JSON Response'})
        return HttpResponse(json_data, content_type="application/json")

    def put(self,  request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is a PUT Method JSON Response'})
        return HttpResponse(json_data, content_type="application/json")

    def delete(self,  request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is a DELETE Method JSON Response'})
        return HttpResponse(json_data, content_type="application/json")
