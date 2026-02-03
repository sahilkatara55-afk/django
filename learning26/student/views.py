from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request,"studentHome.html")
def studentDashboard(request):
    student = {"name":"sahil","age":22,"city":"dahod"}
    return render(request,"student/studentDashboard.html",student) 
#student/studentDashboard.html
    #folder/filename