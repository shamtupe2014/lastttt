from django.db import models

# Create your models here.
class students(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=64)
    stand = models.IntegerField()
    dob = models.DateField()
def __str__(self):
    return self.name