from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeewithforom),
    path('createCourse/',views.createCourse),
    path("feedback/",views.feedback_page,name="feedback"),
    path("complaint/",views.complaint_page,name="complaint"),
]