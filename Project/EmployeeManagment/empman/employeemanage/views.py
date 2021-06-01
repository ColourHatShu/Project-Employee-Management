from employeemanage.forms import EmployeeForm
from employeemanage.models import Employee
from django.shortcuts import render
from .forms import EmployeeForm
from .forms1 import EmployeeSalaryForm
# Create your views here.

def employee_list(request):
    return render(request, "employeemanage/employee_list.html")

def employee_form(request):             #insert and update
    form = EmployeeForm()
    form1 = EmployeeSalaryForm()
    return render(request, "employeemanage/employee_form.html", {'form':form})
   # return render(request, "employeemanage/employee_form.html", {'form':form1})

def employee_delete(request):           #delete
    return
