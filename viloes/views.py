from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def cadastro_v(request):
    if request.method == "GET":
        return render(request, 'cadastro_viloes.html')
    else:
        codinome = request.POST.get('codinome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=codinome).first() # primeiro campo, da lib, segundo, o nosso

        # outras infs

        descricao = request.POST.get('descricao')
        poderes = request.POST.get('poderes')
        foto = request.FILES.get("foto")
        

        if user:
            return HttpResponse('Já existe um user com este codi!')
        
        user = User.objects.create_user(username=codinome, email=email, password=senha)
        user.save()
        perfil = Perfil_viloes(user = user, descricao = descricao, poderes = poderes, foto = foto)
        perfil.save()

        login_django(request, user)

        return redirect('plataforma')

def login_v(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        codinome = request.POST.get('codinome')
        senha = request.POST.get('senha')

        user = authenticate(username=codinome, password=senha)

        if user:
            login_django(request, user)
            return redirect('plataforma')
            
        else:
            return HttpResponse("noooo")
        
def logout_view(request):
    logout(request)
    return redirect('/auth/login') 

def listar(request):
    usuarios = User.objects.all()
    return HttpResponse(usuarios)

@login_required(login_url='/auth/login/')
def plataforma(request):
    return redirect('plataforma')
