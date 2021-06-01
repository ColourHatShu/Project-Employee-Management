from Employee.forms import EmployeeForm
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "Employee/employee_list.html", context)

def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "Employee/employee_form.html", {'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/employee/list')

def employee_delete(request):
    return
