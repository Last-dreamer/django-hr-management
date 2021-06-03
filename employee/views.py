from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import EmployeeForm
from .models import Employees
# Create your views here.



# To create employee
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemp")
            except:
                print('error')
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})


#  to edit an employee
def editemp(request, name):
    employee = Employees.objects.get(name=name)
    return render(request, "editemployee.html", {'employee': employee})



# To update employee details
def updateEmp(request, name):
    if request.method == 'POST':
        employee = Employees.objects.get(name=name)
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            f = form.save()
            return redirect('/showemp')
        else:
            return HttpResponseNotFound("%s" % (form.errors))
        return render(request, "editemployee.html", {'employee': employee})



def deleteEmp(request, name):
    employee = Employees.objects.get(name=name)
    employee.delete()
    return redirect("/showemp")


# to show all employes
def showemp(request):
    employees = Employees.objects.all()
    return render(request, "showemp.html", {'employees': employees})