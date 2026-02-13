from django.db import models

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
