from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
import sweetify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import AgentForm, CaseForm
from .models import agent, Cases

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            sweetify.success(request, '¡Has iniciado sesión!')
            return redirect('home')
        else:
            sweetify.error(request, 'Usuario o contraseña incorrectos')
            print('Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('/')

def casos(request):
    data = {
        'form': CaseForm(),
        'title': 'Casos',
    }

    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, '¡Caso creado correctamente!')
            return redirect('home')
        data['form'] = form
    return render(request, 'form.html', data)


def agente(request):
    data = {
        'form': AgentForm(),
        'title': 'Crear Agente'
    }

    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, '¡Caso creado correctamente!')
            return redirect('home')
        data['form'] = form
    return render(request, 'form.html', data)

def verAgente(request):
    agents = agent.objects.all()
    thead_field = ['Nombre', 'Email', 'Teléfono', 'Dirección', 'Opciones']
    tbody_field = [
        (
            agent.agent_name, 
            agent.agent_email,
            agent.agent_phone,
            agent.agent_address,
            {
                'pk': agent.id,
                'url': reverse('editarAgentes', args=[agent.id]),
                'url_delete': reverse('eliminarAgentes', args=[agent.id]),
             }
        )
        for agent in agents
        ]
    data = {
        'thead_field': thead_field,
        'tbody_field': tbody_field,
        'title': 'Agentes',
    }
    return render(request, 'listar.html', data)

def verCaso(request):
    casos = Cases.objects.all()
    thead_field = ['Asignado a', 'Nombre', 'Descripción', 'Estado', 'Prioridad', 'Fecha de Creación', 'Fecha de Cierre', 'Opciones']
    tbody_field = [
        (
            case.Assigned_to.agent_name, 
            case.case_name, 
            case.case_description, 
            case.case_status, 
            case.case_priority, 
            case.case_created, 
            case.case_closed, 
            {
             'pk': case.id,
             'url': reverse('editarCasos', args=[case.id]),
             'url_delete': reverse('eliminarCasos', args=[case.id]),
            } 
        )
        for case in casos
        ]
    data = {
        'thead_field': thead_field,
        'tbody_field': tbody_field,
        'title': 'Casos'
    }
    return render(request, 'listar.html', data)

def editarAgentes(request, id):
    agentes = get_object_or_404(agent, id=id)
    data = {
        'form': AgentForm(instance=agentes),
        'title': 'Editar Agente'
    }
    if request.method == 'POST':
        form = AgentForm(data=request.POST, instance=agentes)
        if form.is_valid():
            form.save()
            sweetify.success(request, '¡Agente actualizado correctamente!')
            return redirect('verAgente')
        data['form'] = form
    return render(request, 'edit.html', data)


def editarCasos(request, id):
    casos = get_object_or_404(Cases, id=id)
    data = {
        'form': CaseForm(instance=casos),
        'title': 'Editar Caso'
    }
    if request.method == 'POST':
        form = CaseForm(data=request.POST, instance=casos)
        if form.is_valid():
            form.save()
            sweetify.success(request, '¡Caso actualizado correctamente!')
            return redirect('verCaso')
        data['form'] = form
    return render(request, 'edit.html', data)

def eliminarAgentes(request, id):
    agentes = get_object_or_404(agent, id=id)
    agentes.delete()
    sweetify.success(request, '¡Agente eliminado correctamente!')
    return redirect('verAgente')

def eliminarCasos(request, id):
    casos = get_object_or_404(Cases, id=id)
    casos.delete()
    sweetify.success(request, '¡Caso eliminado correctamente!')
    return redirect('verCaso')