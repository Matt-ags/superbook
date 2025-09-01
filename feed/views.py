from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from usuarios.models import *
# Create your views here.
@login_required(login_url='/auth/login/')
def plataforma(request):

    # BUSCANDO DADOS DO USUARIO: 

    user_username = request.user.username # NOME
    user_user_id = request.user.id # ID
    dados_user = Perfil.objects.filter(user_id=user_user_id) # SELECT COM OUTRAS INFORMAÇÕES
    # print(user_username)
    # print(user_user_id)
    # print(dados_user)
    # for dado in dados_user:
    #     print(dado.poderes)
    #     print(dado.descricao)

    if dados_user: # SE CONSEGUIU ACHAR
        user_infs = dados_user[0] # PEGA O QUE ACHOU (é confuso, mas só estamos acessando o dado, que no caso, o primeiro é o que importa)

        poderes = user_infs.poderes # poderes
        descricao = user_infs.descricao # descrição
    
    usuario_cadastrado = { # objeto com as informações bases
        'nome_usuario': user_username,
        'id_usuario': user_user_id,
        'dadosbrutos_usuario': dados_user,
        'poderes_usuario': poderes,
        'descricao_usuario': descricao
    }
    
    return HttpResponse("ok plataforma (a partir do app feed)")