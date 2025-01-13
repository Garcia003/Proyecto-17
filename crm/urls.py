from django.urls import path
from . import views

urlpatterns = [
    path('casos/', views.casos, name='casos'),
    path('agente/', views.agente, name='agente'),
    path('verAgente/', views.verAgente, name='verAgente'),
    path('verCaso/', views.verCaso, name='verCaso'),
    path('editarAgentes/<id>/', views.editarAgentes, name='editarAgentes'),
    path('editarCasos/<id>/', views.editarCasos, name='editarCasos'),
    path('eliminarAgentes/<id>/', views.eliminarAgentes, name='eliminarAgentes'),
    path('eliminarCasos/<id>/', views.eliminarCasos, name='eliminarCasos'),
]