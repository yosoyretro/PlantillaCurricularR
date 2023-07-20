from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html',{})

def olvidarControseña(request):
    return render(request,'',{})

def menu_inicio(request):
    return render(request,'',{})

