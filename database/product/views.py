from django.shortcuts import render
from .models import students,destination,employee

def home1(request):
    std = students.objects.all()
    return render(request, "home1.html",{"std":std})




def index1(request):
    telu = destination.objects.all()
    return render(request,"index1.html",{"telu":telu})

def index(request):
    return render(request,"index.html")

def karvy(request):
    emp = employee.objects.all()
    return render(request,"karvy.html",{"emp":emp})

