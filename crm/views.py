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