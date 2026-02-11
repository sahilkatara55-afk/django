
# Register your models here.
from django.contrib import admin
# from .forms import CourseForm
from .models import Employee,Course, feedback,complaint

# Register your models here.
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(feedback)
admin.site.register(complaint)