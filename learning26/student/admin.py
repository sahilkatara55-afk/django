from django.contrib import admin

# Register your models here.
from .models import Student,Product,Employee,StudentProfile,Category,Service,UserProfile,Vehicle,InspectionReport,Inquiry,TestDrive
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(UserProfile)
admin.site.register(Vehicle)
admin.site.register(InspectionReport)
admin.site.register(Inquiry)
admin.site.register(TestDrive)
