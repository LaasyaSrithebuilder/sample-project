from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee

@login_required
def home(request):
    employees = Employee.objects.all()
    return render(request, 'core/home.html', {'employees': employees})

@login_required
def employee_add(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            salary=request.POST['salary'],
        )
        return redirect('home')
    return render(request, 'core/employee_form.html', {'action': 'Add'})

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('home')
    return render(request, 'core/employee_form.html', {'action': 'Edit', 'employee': employee})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'core/employee_confirm_delete.html', {'employee': employee})