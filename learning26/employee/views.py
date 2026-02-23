from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm,CourseForm,feedbackForm,complaintForm

# from django.shortcuts import render
from .models import Employee
# from .forms import EmployeeForm

# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().order_by("id").values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})#Create your views here.

def employeeFilter(request):
    #where select  from employee where name = "raj"
    employee = Employee.objects.filter(name ="raj").values()
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    #select  from employee where name = "raj" and post = "Developer"
    employee3 = Employee.objects.filter(name ="raja",post ="Developer").values()
    #select  from employee where name = "raj" or post = "Developer"

    #>23
    #seelct  from employee where age > 23
    #employee4 = Employee.objects.filter(age>23).values()
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    #lt , lte

    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()
    #contains
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

    #in
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()    

    #range
    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc

    

    #and
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    print("query 18",employee18)
    return render(request, 'employee/employeeFilter.html')


def createEmployee(request):
    Employee.objects.create(name="ajay",age="23",salary="23000",post="hr",join_date="2024-01-01")

    return HttpResponse("Employee created")
 
def createEmployeewithform(request):
    print(request.method)
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save() #it same as create
            #return HttpResponse("Employee created")
            return redirect("employeeList") #url name from urls.py
    else:
            #from object create ----> html
            form = EmployeeForm()
    return render(request,"employee/createEmployeeForm.html",{"form":form})

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})  

# Feedback (ModelForm)   
def feedback_page(request):
    if request.method == "POST":
        form = feedbackForm(request.POST)
        # if form.is_valid():
        form.save()
        return HttpResponse("Feedback submitted successfully!")
    else:
        form = feedbackForm()
        return render(request, "employee/feedback.html", {"form": form})    
def complaint_page(request):
    if request.method == "POST":
        form = complaintForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database, send email, etc.)
            user_name = form.cleaned_data['user_name']
            problem = form.cleaned_data['problem']
            # Here you can save the complaint to the database or perform other actions
            return HttpResponse("Complaint submitted successfully!")
    else:
        form = complaintForm()
    return render(request, "employee/complaint.html", {"form": form})    
def deleteEmployee(request,id):
    #delete from employee whhere id = 1
    print ("id from url",id)
    Employee.objects.filter(id=id).delete()
    print("delete employee")
    #return HttpResponse("delete employee")
    return redirect("employeeList") #url name from urls.py

def filterEmployee(request):
    print("filter employee called...")
    employees = Employee.objects.filter(age__gte=23).values()
    print("filter Employees =",employees)
    # return redirect ("employeeList")
    return render(request,"employee/employeelist.html",{"employees":employees})

from django.db.models import Q

from django.db.models import Q

def employeeList(request):

    search = request.GET.get('search', '')
    sort = request.GET.get('sort')

    employees = Employee.objects.all()

    # 🔍 Search
    if search:
        employees = employees.filter(
            Q(name__icontains=search) |
            Q(age__icontains=search) |
            Q(post__icontains=search)
        )

    # 📊 Sort
    if sort:
        employees = employees.order_by(sort)

    context = {
        'employees': employees,
        'search': search
    }

    return render(request, 'employee/employeeList.html', context)

#update --->
def updateEmployee(request,id):
    #database existing user... id -->
    employee = Employee.objects.get(id=id) #select * from employee where id = 1
    
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        form.save()
        return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)    
        return render(request,"employee/updateEmployee.html",{"form":form})