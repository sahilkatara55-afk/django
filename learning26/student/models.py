from django.db import models

# Create your models her.
#parent class Model
#create table student(studentName varchar(100),studentAge int,studentCity varchar(40))
#it will generate pk automatically
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name

    def __str__(self):
        return self.studentName 

        
class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"

class Employee(models.Model):

    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "company_employee"   # Table name in PostgreSQL
        ordering = ["-id"]              # Latest record first
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name

class StudentProfile(models.Model):

    # Choices for hobbies
    HOBBY_CHOICES = [
        ("reading", "Reading"),
        ("travel", "Travel"),
        ("music", "Music"),
    ]

    studentId = models.OneToOneField(Student, on_delete=models.CASCADE)

    studentHobbies = models.CharField(
        max_length=100,
        choices=HOBBY_CHOICES
    )

    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"   

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName    

from django.db import models
from django.contrib.auth.models import User

# --- USER PROFILE (1-to-1 Relation) ---
class UserProfile(models.Model):
    # One-to-one relationship with Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# --- CORE TABLES (With Foreign Keys) ---

# Table 1: Vehicle (Foreign Key to User)
class Vehicle(models.Model):
    # Sellers list cars for sale
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    make = models.CharField(max_length=50) 
    model = models.CharField(max_length=50) 
    year = models.PositiveIntegerField() 
    price = models.DecimalField(max_digits=12, decimal_places=2) 
    mileage = models.PositiveIntegerField() 
    description = models.TextField() 
    is_available = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

# Table 2: InspectionReport (Foreign Key to Vehicle)
class InspectionReport(models.Model):
    # Car condition evaluation with AI-powered diagnostics 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='inspections')
    ai_diagnostic_summary = models.TextField() # [cite: 13]
    history_report = models.TextField() 
    is_certified = models.BooleanField(default=False) 

# Table 3: Inquiry (Foreign Key to Vehicle and User)
class Inquiry(models.Model):
    # In-app messaging for buyer-seller communication 
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inquiries')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    message = models.TextField()
    offered_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True) 
    status = models.CharField(max_length=20, default='Pending') # For negotiation [cite: 15]

# Table 4: TestDrive (Foreign Key to Vehicle)
class TestDrive(models.Model):
    # Schedule and manage test drives 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField() 
    status = models.CharField(max_length=20, default='Scheduled')