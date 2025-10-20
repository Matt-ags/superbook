from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from usuarios.models import *
from viloes.models import Perfil_viloes
from posts.models import Post,Pow
# Create your views here.
@login_required(login_url='/auth/login/')
def plataforma(request):
    perfil = None
    tipo = "heroi"

    # Tenta pegar perfil de herói
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        # Se não for herói, tenta pegar perfil de vilão
        try:
            perfil = Perfil_viloes.objects.get(user=request.user)
            tipo = "vilao"
        except Perfil_viloes.DoesNotExist:
            pass

    posts = Post.objects.all()

    return render(request, 'feed.html', {
        'perfil': perfil,
        'posts': posts,
        'tipo_perfil': tipo,  # 🔥 adiciona essa variável
    })


@login_required(login_url='/auth/login/')
def criar_post(request):

    # BUSCANDO DADOS DO USUARIO: 

    perfil = None
    tipo = "heroi"

    # Tenta pegar perfil de herói
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        # Se não for herói, tenta pegar perfil de vilão
        try:
            perfil = Perfil_viloes.objects.get(user=request.user)
            tipo = "vilao"
        except Perfil_viloes.DoesNotExist:
            pass

    user_username = request.user.username # NOME
    user_user_id = request.user.id # ID
    dados_user = Perfil.objects.filter(user_id=user_user_id) # SELECT COM OUTRAS INFORMAÇÕES

    poderes = ""
    descricao = ""
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
        'descricao_usuario': descricao,
        'perfil': perfil,
        'tipo_perfil': tipo, 
    }

    if request.method == "POST":
        mensagem = request.POST.get('mensagem')
        autor = request.user
        Post.objects.create(
            autor=autor,
            mensagem=mensagem
            # não precisa passar criado_em, o Django faz sozinho
        )
    
    return render(request, 'criar_post.html', usuario_cadastrado)

@login_required(login_url='/auth/login/')
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    like, created = Pow.objects.get_or_create(autor=user, post=post)

    if not created:
            # já tinha curtido → remove (toggle)
        like.delete()
    return redirect("plataforma")

def logout_view(request):
    logout(request)
    return redirect('login')