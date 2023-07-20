from django.contrib import admin
from django.urls import path
from processos import views
urlpatterns = [
    path('',views.login,name='login'),
    path('inicio',views.menuInicio,name='Inicio'),
    path('olvide Controseña/',views.olvidarControseña,name='olvideContraseña'),
    path('admin/', admin.site.urls),
]
