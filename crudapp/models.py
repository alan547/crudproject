from django.db import models

# Create your models here.
class Employee(models.Model):
    employ_name=models.CharField(max_length=255,null=True)
    department=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    contact_number=models.CharField(max_length=255,null=True)
    