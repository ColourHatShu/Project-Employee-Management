from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname':'Full Name',
            'emp_code':'Emp_Code',
           
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        self.fields['salary'].empty_label = "Select"
        self.fields['emp_code'].required = False
    
        
