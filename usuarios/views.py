from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import UserForm, PerfilForm
# Create your views here.

def cadastro(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            login_django(request, user)
            
    else:
        user_form = UserForm()
        perfil_form = PerfilForm()

    return render(request, 'cadastro.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        codinome = request.POST.get('codinome')
        senha = request.POST.get('senha')

        user = authenticate(username=codinome, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("OK")
            
        else:
            return HttpResponse("noooo")

@login_required(login_url='/auth/login/')
def plataforma(request):
    return HttpResponse("ok plataforma")