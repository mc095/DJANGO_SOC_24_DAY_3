from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Employee, Department, Role

def index(request):
    return render(request, 'index.html')

def add_emp(request):
    
    # form details fetching
    if request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone_number = request.POST['phone_number']
        hire_date = request.POST['hire_date']
        dept_id = request.POST['dept']
        role_id = request.POST['role']
        
        # creating an object for the recieved attributes
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone_number=phone_number,
            hire_date=hire_date,
            dept_id=dept_id,
            role_id=role_id,
        )
        
        employee.save()
        
    
        return HttpResponse("""
                            <html>
                                <h2>New Employee has been added!</h2>
                            </html>
                            """)

    departments = Department.objects.all()
    roles = Role.objects.all()
    
    context = {
        'departments': departments,
        'roles': roles,
    }
    
    return render(request, 'add_emp.html', context)

def remove_emp(request):
    employee = None  # Initialize variable to hold employee info

    if request.method == "POST":
        sno = request.POST.get('sno')  # Get the sno from the form

        try:
            # Fetch employee using sno
            employee = Employee.objects.get(sno=sno)  # Get the employee by sno
            
            # Check if the confirm button was pressed
            if request.POST.get('confirm') == "true":  
                employee.delete()  # Delete the employee
                return HttpResponse("""<h2 style="text-align: center;">Employee has been removed successfully!</h2>""")
        
        except Employee.DoesNotExist:
            return HttpResponse("""<h2 style="text-align: center;">Employee with the given Serial Number not found. Please try again.</h2>""")

    return render(request, 'remove_emp.html', {'employee': employee})  # Pass employee info to template


def filter_emp(request):
    emp_list = Employee.objects.all()
    context = {
        'emp_list': emp_list,
    }
    return render(request, 'filter_emp.html', context)



def view_all_emp(request):
    template = loader.get_template('view_all_emp.html')
    
    emp_list = Employee.objects.all()
    context = {
        'emp_list' : emp_list,
    }
    
    return HttpResponse(template.render(context, request))


