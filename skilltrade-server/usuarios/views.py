from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('blog:inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('blog:inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('blog:inicio')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado exitosamente!')
            return redirect('usuarios:perfil')
    else:
        form = UserCreationForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
