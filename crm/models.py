from django.db import models

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class agent(models.Model):
    agent_name = models.CharField(max_length=150, verbose_name="Nombre del Agente")
    agent_email = models.EmailField(verbose_name="Correo del Agente")
    agent_phone = models.CharField(max_length=15, verbose_name="Teléfono del Agente")
    agent_address = models.TextField(verbose_name="Dirección del Agente")
    agent_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación del Agente")
    agent_updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización del Agente")

    def __str__(self):
        return self.agent_name
    
class Cases(models.Model):
    Assigned_to = models.ForeignKey(agent, on_delete=models.CASCADE, verbose_name="Asignado a")
    case_name = models.CharField(max_length=150, verbose_name="Nombre del Caso")
    case_description = models.TextField(verbose_name="Descripción del Caso")
    case_status = models.CharField(max_length=50, verbose_name="Estado del Caso")
    case_priority = models.CharField(max_length=50, verbose_name="Prioridad del Caso")
    case_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación del Caso")
    case_updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización del Caso")
    case_closed = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Cierre del Caso")

    def __str__(self):
        return self.case_name