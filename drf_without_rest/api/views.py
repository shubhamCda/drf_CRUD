from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.core.serializers import serialize

# Create your views here.
# EmployeeDataCBV --> API
# class EmployeeDataCBV(View):
#     def  get(self, request, id, *args, **kwargs):
#         # return HttpResponse("This is a GET Method")
#         emp = Employee.objects.get(id=id)
#         emp_data = {
#             'Emp_No':emp.eno,
#             'Name':emp.ename,
#             'Salary':emp.esal,
#             'Address':emp.eaddr
#         }
#         json_data = json.dumps(emp_data)
#         return HttpResponse(json_data, content_type= "application/json")

# API -> By using Serializer in Django inbuilt module Serializers
class EmployeeDataCBV(View):
    def  get(self, request, id, *args, **kwargs):
        # return HttpResponse("This is a GET Method")
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp], fields=('eno','ename', 'eaddr'))
        
        return HttpResponse(json_data, content_type= "application/json")