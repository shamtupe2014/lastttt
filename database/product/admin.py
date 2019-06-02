from django.contrib import admin
from.models import students
# Register your models here.




class studentAdmin(admin.ModelAdmin):
    list_display = ["rollno","name","stand","dob"]

admin.site.register(students,studentAdmin)