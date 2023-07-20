from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        return redirect('Inicio')
    else:
        return render(request,'login.html',{})

def olvidarControseña(request):
    return render(request,'',{})

def menuInicio(request):
    return render(request,'dashboard.html',{})

