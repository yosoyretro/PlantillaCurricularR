from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    return render(request, 'login.html', {})

def forgot_view(request):
    return render(request, 'forgot.html', {})

def recover_view(request):
    return render(request, 'recoverpsw.html',{})

def dashboard_view(request):
    return render(request, 'dashboard.html',{})

def asignatura_view(request):
    return render(request, 'asignatura.html',{})

def trabajador_view(request):
    return render(request, 'Registrar.html', {})

def versiones_view(request):
    return render(request, 'versiones.html',{})    

def referencias_view(request):
    return render(request, 'referencias.html',{})