from rest_framework import serializers
from .models import Employee
#from .models import EmployeeSalary

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# class EmployeeSalarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeSalary
#         fields = '__all__'

