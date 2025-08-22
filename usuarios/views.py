from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        codinome = request.POST.get('codinome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=codinome).first() # primeiro campo, da lib, segundo, o nosso

        if user:
            return HttpResponse('Já existe um user com este codi!')
        
        user = User.objects.create_user(username=codinome, email=email, password=senha)
        user.save()

        return HttpResponse("cadastrado ok!")

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