from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm



def login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso")
                return redirect('home')  # Reemplaza 'home' con la URL de tu página de inicio
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Por favor, corrija los errores en el formulario")
    else:
        form = LoginForm()
    
    # Pasamos el username al contexto para usarlo en la plantilla
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    
    return render(request, 'login/login.html', {'form': form, 'username': username})


def index(request):
    
    context = {'nombre': 'Juan', 'edad': 30}
    return render(request, 'login/login.html',context)
