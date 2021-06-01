from django import forms
from .models import Employee
from .models import EmployeeSalary


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSalaryForm(forms.ModelForm):

    class Meta:
        model = EmployeeSalary
        fields = '__all__'

