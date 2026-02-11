from django.db import models

# Create your models here.
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    
class Course(models.Model):
     name = models.CharField(max_length=100)
     fee = models.IntegerField()
     duration = models.IntegerField()
     class Meta:
        db_table = "course"
     def __str__(self):
        return self.name
     
class feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=5)
    comment = models.TextField()

    class Meta:
        db_table = "feedback"

    def __str__(self):
        return self.name

# Create your models here.
class complaint(models.Model):
    user_name = models.CharField(max_length=100)
    problem = models.TextField()
    status = models.CharField(max_length=100,default="pending")

    class Meta:
        db_table = "complaint"
    def __str__(self):
        return self.user_name    
         