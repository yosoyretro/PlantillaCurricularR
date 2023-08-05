"""
URL configuration for sistema_academico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from processos import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('recover/', views.recover_view, name='recover'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('datosinformativos/', views.datosinfo_view, name='datosinfo'),
    path('trabajador', views.trabajador_view, name='trabajador'),
    path('producto/', views.producto_view, name='producto'),
    path('referencias/', views.referencias_view, name='referencias'),
    path('docente/', views.docente_view, name='docente'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('configuracion/', views.configuracion_view, name='configuracion'),
    path('unidades/', views.unidades_view, name='unidades'),
    path('admin/', admin.site.urls),
]
