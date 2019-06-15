from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('home1/',views.home1,name="home"),
    path('index1/',views.index1,name="index1"),
    path('',views.index,name="index"),
    path('karvy/',views.karvy,name="karvy"),
    ]

