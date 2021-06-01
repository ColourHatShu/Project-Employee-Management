from employeemanage.forms import EmployeeForm
from employeemanage.models import EmployeeSalary
from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def employee_list(request):
    return render(request, "employeemanage/employee_list.html")

def employee_form(request):             #insert and update
    form = EmployeeForm()
    return render(request, "employeemanage/employee_form.html", {'form':form})

def employee_form(request):
    form1 =EmployeeSalary
    return render(request,"employeemanage/employee_form.html", {'form':form1})


def employee_delete(request):           #delete
    return
