
from django.db import models

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length=250)
    employee = models.OneToOneField("Employees", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Employees(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, null=True)
    cnic = models.CharField(max_length=100, null=True, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



