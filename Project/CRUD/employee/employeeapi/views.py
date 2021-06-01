from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeRegistration
from .models import User
# Create your views here.

#This function will add new Item and Show all items
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = EmployeeRegistration()
           
    else: 
        fm = EmployeeRegistration()
    emp = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form' : fm, 'empo': emp})

#This Function Will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
         fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
    return render(request,'enroll/updateemployee.html',{'form':fm})

#This Function Will Delete
def delete_data(request, id):
    if request.method == 'POST':
      pi = User.objects.get(pk=id)     #pk = primary key
      pi.delete()
      return HttpResponseRedirect('/')
