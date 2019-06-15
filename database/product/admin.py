from django.contrib import admin
from.models import students,destination,employee
# Register your models here.




class studentsAdmin(admin.ModelAdmin):
    list_display = ["rollno","name","stand","dob"]

class destinationAdmin(admin.ModelAdmin):
    list_display = ["Name","Desc","Img","Price"]

class employeeAdmin(admin.ModelAdmin):
    list_display = ["Name","Emp_No","Email_ID","Mobile_No","Designation","DOJ","DOB","Photo","Remark"]





admin.site.register(students,studentsAdmin)
admin.site.register(destination,destinationAdmin)
admin.site.register(employee,employeeAdmin)