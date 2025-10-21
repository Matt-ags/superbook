from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from usuarios.models import *
from viloes.models import *
from posts.models import Post
# Create your views here.

    
@login_required(login_url='/auth/login/')
def perfil(request):

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
            perfil = User.objects.filter()

    posts = Post.objects.filter(autor=request.user).order_by('-criado_em')  # só posts dele
    return render(request, 'perfil.html', {'perfil': perfil, 'posts': posts, 'tipo_perfil': tipo})

@login_required(login_url='/auth/login/')
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        novo_mensagem = request.POST.get('mensagem')
        post.mensagem = novo_mensagem
        post.save()
        # TO DO: melhorar a forma de redirecionamento 
    # BUSCANDO DADOS DO USUARIO: 

    user_username = request.user.username # NOME
    user_user_id = request.user.id # ID
    dados_user = Perfil.objects.filter(user_id=user_user_id) # SELECT COM OUTRAS INFORMAÇÕES
    posts = Post.objects.filter(autor_id=user_user_id) 

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
    
    return render(request, 'editar_post.html', {'usuario_cadastrado': usuario_cadastrado, 'post': post})

