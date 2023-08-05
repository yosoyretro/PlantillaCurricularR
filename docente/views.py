from django.shortcuts import render
from processos.models import Asignatura


# Create your views here.
def docente_view(request):

    return render(request, 'dbs_docente.html',)

def  versiones_view(request):
    return render(request, 'versiones.html', {})

def  microcurricular_view(request):
    objasignatura = Asignatura.objects.filter(estado="A")
    
    return render(request, 'microcurricular.html',{'asignatura':objasignatura})

def perfildc_view(request):
    return render(request, 'perfil_docente.html', {})

def configuraciondc_view(request):
    return render(request, 'configuraciondc.html', {})


