from django.db import models

# Create your models here.
class students(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=64)
    stand = models.IntegerField()
    dob = models.DateField()
def __str__(self):
    return self.name

class destination(models.Model):
    Name = models.CharField(max_length=64)
    Img = models.ImageField(upload_to='pic')
    Desc = models.TextField()
    Price = models.IntegerField()

class employee(models.Model):
    Name = models.CharField(max_length=100)
    Emp_No = models.IntegerField()
    Email_ID = models.EmailField()
    Mobile_No = models.IntegerField()
    Designation = models.CharField(max_length=64)
    DOJ = models.DateField()
    DOB = models.DateField()
    Photo = models.ImageField(upload_to='pic')
    Remark = models.TextField()

