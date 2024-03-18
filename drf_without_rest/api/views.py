import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Employee
# import json
# from django.core.serializers import serialize
from api.mixins import SerializeMixin, HttpResponseMixin

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

#############################################################################

# API -> By using Serializer in Django inbuilt module Serializers
# Serialization-> to convert py obj into JSON -- can be perform in two ways :
#                  1. Using JsonSerializer()
#                  2. Using rest_framework
# class EmployeeDataCBV(SerializeMixin, View):
#     def  get(self, request, id, *args, **kwargs):
#         # return HttpResponse("This is a GET Method")
                       
#         # json_data = serialize('json', [emp], fields=('eno','ename', 'eaddr'))

#         # by using mixins
#         json_data = self.serialize([emp])
        
#         return HttpResponse(json_data, content_type= "application/json")

################################################################################

# # Exception Handling 
            
#################################################################################            
            
# Exception Handling at  the Application Level

# class EmployeeDataCBV(SerializeMixin, View):
#     def  get(self,request,id,*args,**kwargs):
#            emp = Employee.objects.get(id=id)
#            json_data = self.serialize([emp])
          
#            return HttpResponse(json_data,content_type="application/json")


# Exception Handling at  the Project Level

class EmployeeDataCBV(HttpResponseMixin, SerializeMixin, View):
    def  get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except  Employee.DoesNotExist:
            json_data = json.dumps({'msg':"Employee Does not Exists"})
            # return HttpResponse(json_data, content_type= "application/json", status=404)
            return self.render_to_http_res(json_data, status=404) # By using HttpResponseMixin
        else:
            json_data = self.serialize([emp])
            # return HttpResponse(json_data,content_type="application/json", status=200)
            return self.render_to_http_res(json_data)
            
            
#################################################################################            
            
# Here Problem is ->(model & pk) {'model': 'api.employee', 'pk': 1, 'fields': {'eno': 101, 'ename': 'shubham'}},    
# class EmployeeListCBV(View):
#     def get(self,request,*args,**kwargs):
#         emps = Employee.objects.all()
#         json_data = serialize('json',emps,fields=('eno','ename') )
#         return HttpResponse(json_data,content_type="application/json")

        
# Solving aboves Problem ,    
# class EmployeeListCBV(View):
#     def get(self,request,*args,**kwargs):
#         emps = Employee.objects.all()
#         json_data = serialize('json',emps,fields=('eno','ename') )
#         p_data = json.loads(json_data)
#         final_list = []
#         for obj in p_data:
#             emp_data = obj['fields']
#             final_list.append(emp_data)
#         json_data = json.dumps(final_list)
#         return HttpResponse(json_data,content_type="application/json")

#############################################################################

# By using MIXINS method by mixins.py--> reducing aboves code and inc reusability
class EmployeeListCBV(SerializeMixin, View):
    def get(self,request,*args,**kwargs):
        emps = Employee.objects.all()
        json_data = self.serialize(emps )
        # p_data = json.loads(json_data)
        # final_list = []                    NO
        # for obj in p_data:                 NEED
        #     emp_data = obj['fields']       THIS
        #     final_list.append(emp_data)    CODE
        # json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type="application/json")