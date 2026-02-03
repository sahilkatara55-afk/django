from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render (request,"home.html")

def aboutus(request):
    return render (request,"aboutus.html")

def contactus(request):
    return render (request,"contactus.html")

def reacp(request):
    return render (request,"reacp.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient} 
    return render(request,"recipe.html",data)