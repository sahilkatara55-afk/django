from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeewithforom,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse),
    path("feedback/",views.feedback_page,name="feedback"),
    path("complaint/",views.complaint_page,name="complaint"),
   # path("deleteEmployee/",views.deleteEmployee,name="deleteEmployee"),
    path("deleteEmployee/<int:id>/",views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
]