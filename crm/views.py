from pyexpat.errors import messages
from django.shortcuts import redirect, render
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
    thead_field = ['Nombre', 'Email', 'Teléfono', 'Dirección']
    tbody_field = [
        (agent.agent_name, agent.agent_email,
        agent.agent_phone,agent.agent_address)
        for agent in agents
        ]
    data = {
        'thead_field': thead_field,
        'tbody_field': tbody_field,
        'title': 'Agentes'
    }
    return render(request, 'listar.html', data)

def verCaso(request):
    casos = Cases.objects.all()
    thead_field = ['Asignado a', 'Nombre del Caso', 'Descripción del Caso', 'Estado del Caso', 'Prioridad del Caso', 'Fecha de Creación del Caso', 'Fecha de Cierre del Caso']
    tbody_field = [
        (case.Assigned_to, case.case_name, case.case_description, case.case_status, case.case_priority, case.case_created, case.case_closed)
        for case in casos
        ]
    data = {
        'thead_field': thead_field,
        'tbody_field': tbody_field,
        'title': 'Casos'
    }
    return render(request, 'listar.html', data)