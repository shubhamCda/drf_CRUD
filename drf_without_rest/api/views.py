import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import EmployeeForm
from api.utils import is_json
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDataCBV(HttpResponseMixin, SerializeMixin, View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp 

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

    # implement PUT method
    def put(self, request,id, *args, **kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Invalid Employee ID'})
            return self.render_to_http_res(json_data,status=404)
        data = request.body
        valid_json = is_json(data)
        if  not valid_json:
            json_data=json.dumps({'error':'Bad Request : JSON Data Required'})
            return self.render_to_http_res(json_data,status=400)
        p_data=json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(p_data)
        form=EmployeeForm(original_data, instance=emp) #instance=emp will set the values of fields to existing record(DB)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Updated successfully.....'})
            return self.render_to_http_res(json_data,status=201)
        if form.errors:
            json_data=json.dumps({'error':form.errors})
            return self.render_to_http_res(json_data,status=400)


    # Implement DELETE Method
    def delete(self,request, id,*args,**kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({"message":"Employee does not exist"})
            return self.render_to_http_res(json_data, status=404)
        
        # t = emp.delete()  
        # print(t)  # it will return tuple -> (1, {'api.Employee': 1}) 1-> status, {'api.Employee': 1} -> employee object

        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({ "message": "Deleted Successfully", "deleted item": deleted_item })
            return self.render_to_http_res(json_data, status=200)
            
        json_data = json.dumps({'msg':'Resource  deleted Successfully..!'})
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
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(SerializeMixin,HttpResponseMixin, View):
    def get(self,request,*args,**kwargs):
        emps = Employee.objects.all()
        json_data = self.serialize(emps )
        # p_data = json.loads(json_data)
        # final_list = []                    NO   (replaced with SerializeMixin)
        # for obj in p_data:                 NEED
        #     emp_data = obj['fields']       THIS
        #     final_list.append(emp_data)    CODE
        # json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type="application/json")
    @csrf_exempt
    def post(self, requset, *args, **kwargs):
        data = requset.body  # if you want to post data from external app
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({"error":"Invalid Json Data"})
            return self.render_to_http_res(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource is created...'})
            return self.render_to_http_res(json_data,status=201)
        if form.errors:
            json_data= json.dumps(form.errors)
            return self.render_to_http_res(json_data,status=400)
