from django import forms
from .models import EmployeeSalary

class EmployeeSalaryForm(forms.ModelForm):

    class Meta:
        model = EmployeeSalary
        fields = '__all__'