from django.urls import path
from . import views

urlpatterns = [
    path('casos/', views.casos, name='casos'),
    path('agente/', views.agente, name='agente'),
]