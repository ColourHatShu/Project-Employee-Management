from django.db import models

# Create your models here.

# class EmployeeSalary(models.Model):
#     EmpId = models.CharField(max_length=3)
#     salary = models.CharField(max_length=100)
    
  
#     def __str__(self):
#         return self.EmpId
    
#     def __str__(self):
#         return self.salary

class Employee(models.Model):
    #emp_id = models.CharField(max_length=5)
    fullname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    #CRUD
    #Create / Insert / Add - POST
    #Retrieve / Fetch - GET
    #Update / Edit - PUT
    #Delete / Remove - DELETE
    