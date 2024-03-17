from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.core.serializers import serialize

# Create your views here.
# EmployeeDataCBV --> API
# class EmployeeDataCBV_01(View):
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
# Serialization-> to convert py obj into JSON -- can be perform in two ways :
#                  1. Using JsonSerializer()
#                  2. Using rest_framework
class EmployeeDataCBV(View):
    def  get(self, request, id, *args, **kwargs):
        # return HttpResponse("This is a GET Method")
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp], fields=('eno','ename', 'eaddr'))
        
        return HttpResponse(json_data, content_type= "application/json")

# Here Problem is ->(model & pk) {'model': 'api.employee', 'pk': 1, 'fields': {'eno': 101, 'ename': 'shubham'}},    
class EmployeeListCBV(View):
    def get(self,request,*args,**kwargs):
        emps = Employee.objects.all()
        json_data = serialize('json',emps,fields=('eno','ename') )
        return HttpResponse(json_data,content_type="application/json")