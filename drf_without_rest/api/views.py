from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json

# Create your views here.
class EmployeeDataCBV(View):
    def  get(self, request, id, *args, **kwargs):
        # return HttpResponse("This is a GET Method")
        emp = Employee.objects.get(id=id)
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esalary':emp.esal,
            'eaddr':emp.eaddr
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type= "application/json")