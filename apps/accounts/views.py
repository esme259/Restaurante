from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Aquí iría la lógica de autenticación del usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            # Autenticación y redirección según sea necesario
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                
                # Redirigir a la página principal o a la que corresponda
                return redirect('index_user')
            else:
                form.add_error(None, 'Credenciales inválidas')
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('main_index')