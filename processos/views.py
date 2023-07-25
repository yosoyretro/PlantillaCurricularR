from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def forgot_view(request):
    return render(request, 'forgot.html')

def recover_view(request):
    return render(request, 'recoverpsw.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def planificacion_view(request):
    return render(request, 'planificacion.html')

def versiones_view(request):
    return render(request, 'versiones.html')