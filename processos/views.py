from django.shortcuts import redirect, render
from .models import Trabajador, Asignatura, Referencias, ProductoAcademico
from django.db import transaction

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
    datosAsignatura = Asignatura.objects.filter(estado='A')
    msg = ""

    if request.method == 'POST' and "crear" in request.POST:
        asignatura = request.POST["nombre_asig"]
        objetivo = request.POST["objetivo_asig"]
        aportes = request.POST["aportes_teori"]
        objetivos_es = request.POST["objetivos_especi"]
        producto_ac = request.POST["producto_academ"]
        prerequisitos = request.POST["prerequisitos_acade"]
        periodo_a = request.POST["periodo_asig"]

        asignatura = Asignatura(
            nombre_asignatura=asignatura,
            objetivo_asignatura=objetivo,
            aportes_teoricos=aportes,
            objetivos_especificos=objetivos_es,
            producto_academico=producto_ac,
            prerequisito_academico=prerequisitos,
            periodo=periodo_a
        )
        asignatura.save() 
    return render(request, 'asignatura.html',{'datosAsignatura':
    datosAsignatura, 'msg': msg})

@transaction.atomic
def trabajador_view(request):
    datosTrabajador = Trabajador.objects.filter(estado='A')
    msg = ""
    msg1=""

    if request.method == 'POST':
        if "eliminar" in request.POST:
            trabajador_id = request.POST["eliminar"]
            try:
                trabajador = Trabajador.objects.get(id=trabajador_id)
                trabajador.estado = "I"
                trabajador.save()
                msg = "Trabajador eliminado exitosamente."
            except Trabajador.DoesNotExist:
                msg = "El trabajador no existe o ya ha sido eliminado."

        if "crear" in request.POST:
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
            msg1 = "Trabajador creado exitosamente."
    return render(request, 'Registrar.html', {'datosTrabajador': datosTrabajador, 'msg': msg, 'msg1':msg1})

def producto_view(request):
    datosProducto = ProductoAcademico.objects.filter(estado='A')
    msg = ''

    if request.method == 'POST' and "crear" in request.POST:
        producto_f = request.POST["producto_final"]
        objetivo_p = request.POST["objetivo"]
        producto_p = request.POST["producto_parci"]
        resultados_p = request.POST["resultados_presen"]
        integracion_as = request.POST["integracion_asigna"]

        producto = ProductoAcademico(
            producto_final=producto_f,
            objetivo=objetivo_p,
            producto_parcial=producto_p,
            presentacion=resultados_p,
            integracion=integracion_as
        )
        producto.save()
    return render(request, 'producto.html',{'datosProducto': datosProducto, 'msg':msg})    

def referencias_view(request):
    datosReferencias = Referencias.objects.filter(estado='A')
    msg = ""

    if request.method == 'POST' and "crear" in request.POST:
        referencia = request.POST["tipo_referen"]
        numero_ref = request.POST["numero_referen"]
        titulo = request.POST["titulo_obra"]
        biblioteca = request.POST["existencia_biblioteca"]
        numero = request.POST["numero_ejemplar"]

        referencias = Referencias(
            tipo_referencia=referencia,
            numero_referencia=numero_ref,
            titulo_obra=titulo,
            existencia_biblioteca=biblioteca,
            numero_ejemplares=numero
        )
        referencias.save()
    return render(request, 'referencias.html',{'datosReferencias':
    datosReferencias, 'msg': msg})