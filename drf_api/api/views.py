from django.shortcuts import render

# Create your views here.
def emp_data_view(request):
    EmpData = {
        'eno': 101,
        'ename': 'Shubh',
        'esal': 10000,
        'eaddr': 'Nagpur'
    } 

    resp = f"<h1>Emp Number : {EmpData['eno']}<br>Emp Name : {EmpData['ename']}<br>Emp Salary : {EmpData['eno']}<br>Emp Number : {EmpData['eno']}<br>"