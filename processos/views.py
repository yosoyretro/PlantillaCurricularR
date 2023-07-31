from django.shortcuts import redirect, render
from .models import Trabajador

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
    datosTrabajador = Trabajador.objects.filter(estado='A')
    msg = "Registro exitoso"

    if request.method == 'POST' and "crear" in request.POST:
        nombres_trab = request.POST["nombres_trab"]
        apellidos_trab = request.POST["apellidos_trab"]
        cedula_trab = request.POST["cedula_trab"]
        correo_trab = request.POST["correo_trab"]
        contrasena_trab = request.POST["contrasena_trab"]
        rol_trab = request.POST["rol_trab"]

        trabajador = Trabajador(
            nombres=nombres_trab,
            apellidos=apellidos_trab,
            cedula_identidad=cedula_trab,
            correo=correo_trab,
            contrasena=contrasena_trab,
            rol=rol_trab
        )
        trabajador.save()
    return render(request, 'Registrar.html', {'datosTrabajador': datosTrabajador, 'msg': msg})

def versiones_view(request):
    return render(request, 'versiones.html',{})    

def referencias_view(request):
    return render(request, 'referencias.html',{})