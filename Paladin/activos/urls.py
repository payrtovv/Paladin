from django.urls import path
from . import views

urlpatterns = [
    path(
        'CrearActivo/',
        views.crear_activo,
        name='crear_activo'
    ),

    path(
        '',
        views.lista_activos,
        name='lista_activos'
    ),

    path(
    'eliminar/<int:id>/',
    views.eliminar_activo,
    name='eliminar_activo'
),
]