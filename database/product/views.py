from django.shortcuts import render
from .models import students

def home(request):
    std = students.objects.all()
    return render(request, "home.html",{"std":std})




def index(request):
    return render(request,"home.html")