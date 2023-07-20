from django.contrib import admin
from django.urls import path
from processos import views
urlpatterns = [
    path('/',views.login,name='login'),
    path('inicio/',views.menu_inicio,name='menuInicio'),
    path('olvide Controseña/',views.olvidarControseña,name='olvideContraseña'),
]
