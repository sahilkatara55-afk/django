from django.contrib import admin

# Register your models here.
from .models import Student,Product
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
