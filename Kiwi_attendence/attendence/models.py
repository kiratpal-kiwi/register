import uuid

from django.db import models


# Create your models here.
class RegisterUser(models.Model):
    Emp_id = models.CharField(max_length=50, null=True, blank=True)
    FullName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True, null=True, blank=True)
    Designation = models.CharField(max_length=50)
    Org = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    ContactNumber = models.CharField(max_length=10)
    Department = models.CharField(max_length=50)






