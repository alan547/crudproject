from django.shortcuts import render,redirect
from .import views
from crudapp.models import Employee

# Create your views here.
def show_employee(request):
    return render(request,"employee.html")
def add_employee(request):
    if request.method=='POST':
        ename=request.POST['employee_name']
        dept=request.POST['employee_dept']
        age=request.POST['employee_age']
        email=request.POST['employee_email']
        number=request.POST['contact_num']
        emp=Employee(employ_name=ename,department=dept,age=age,email=email,contact_number=number)
        emp.save()
        return redirect('show_employee_details')
def show_employee_details(request):
    employee=Employee.objects.all()
    return render(request,"show_employee.html",{'emp':employee})
def editpage(request,pk):
    emp=Employee.objects.get(id=pk)
    return render(request,"edit.html",{'employee':emp})
def edit_employee_details(request,pk):
    if request.method=='POST':
        emp=Employee.objects.get(id=pk)
        emp.employ_name=request.POST.get('emp_name')
        emp.department=request.POST.get('dept_name')
        emp.age=request.POST.get('age')
        emp.email=request.POST.get('email')
        emp.contact_number=request.POST.get('contact_num')
        emp.save()
        return redirect('show_employee_details')
    return render(request,"edit.html")
def deletepage(request,pk):
    emp=Employee.objects.get(id=pk)
    emp.delete()
    return redirect('show_employee_details')