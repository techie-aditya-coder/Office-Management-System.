from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
# Create your views here.
from datetime import datetime
from django.db import models
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])       
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary , bonus=bonus, dept_id=dept, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return HttpResponse("An Exception Occured!!Employee Has not Been Added")
    

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:

            return HttpResponse("please Enter a valid Employee id")
        
    emps = Employee.objects.all
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        
        context = {

            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        HttpResponse('An Exception Occured!!')