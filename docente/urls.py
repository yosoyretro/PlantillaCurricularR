from django.contrib import admin
from django.urls import path
from docente import views


app_name= "docente"
urlpatterns = [
    path('',views.docente_view, name='docente'),
    path('veriones/', views.versiones_view, name='versiones'),
    path('planificacion/', views.microcurricular_view, name="planificacion"),
    path('perfil/', views.perfildc_view, name='perfil'),
    path('configuracion/', views.configuraciondc_view, name='configuracion')
]
