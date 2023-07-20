from django.contrib import admin
from django.urls import path
from processos import views
urlpatterns = [
    path('',views.login,name='login'),
    path('inicio',views.menuInicio,name='Inicio'),
    path('versiones',views.versiones,name='Versiones'),
    path('planificacion',views.planificacion,name='Planificacion'),
    path('olvide Controseña/',views.olvidarControseña,name='olvideContraseña'),
    path('admin/', admin.site.urls),
]
