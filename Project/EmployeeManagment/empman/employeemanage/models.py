from django.db import models

# Create your models here.

class EmployeeSalary(models.Model):
    empid = models.CharField(max_length=3)
    salary = models.CharField(max_length=100)
    
    



class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    deparment = models.CharField(max_length=100)
    #empid = models.ForeignKey(EmployeeSalary, on_delete=models.CASCADE)
    salary = models.ForeignKey(EmployeeSalary, on_delete=models.CASCADE)            #with cascade if the data from employeesalary table gets deleted, it will also get deleted in employee table