from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
        queryset = models.Employee.objects.all()
        serializer_class = serializers.EmployeeSerializer

# class EmployeeSalaryViewset(viewsets.ModelViewSet):
#         queryset = models.EmployeeSalary.objects.all()
#         serializer_class = serializers.EmployeeSalarySerializer