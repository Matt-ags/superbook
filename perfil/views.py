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
def editar_perfil(request):

    perfil = None
    tipo = None
    profile_exists = True

    # 1. VERIFICA O PERFIL (Lógica GET) - Sem mudanças
    try:
        perfil = Perfil.objects.get(user=request.user)
        tipo = "heroi"
    except Perfil.DoesNotExist:
        try:
            perfil = Perfil_viloes.objects.get(user=request.user)
            tipo = "vilao"
        except Perfil_viloes.DoesNotExist:
            perfil = None
            profile_exists = False 
            
    # 2. PROCESSA O FORMULÁRIO (Lógica POST)
    if request.method == 'POST':
        # Pega os dados de texto
        descricao_data = request.POST.get('descricao')
        poderes_data = request.POST.get('poderes', 'Nenhum')
        
        # MUDANÇA AQUI: Pega o arquivo de imagem
        # request.FILES é onde as imagens chegam, não request.POST
        foto_data = request.FILES.get('foto', None) # Pega 'None' se nenhum arquivo for enviado

        if profile_exists:
            # --- MODO ATUALIZAÇÃO ---
            perfil.descricao = descricao_data
            perfil.poderes = poderes_data
            
            # MUDANÇA AQUI: Só atualiza a foto se uma NOVA foto foi enviada
            if foto_data:
                perfil.foto = foto_data
                
            perfil.save()
        
        else:
            # --- MODO CRIAÇÃO ---
            tipo_data = request.POST.get('tipo_perfil')

            if tipo_data == 'heroi':
                Perfil.objects.create(
                    user=request.user,
                    descricao=descricao_data,
                    poderes=poderes_data,
                    foto=foto_data  # MUDANÇA AQUI: Adiciona a foto
                )
            elif tipo_data == 'vilao':
                 Perfil_viloes.objects.create(
                    user=request.user,
                    descricao=descricao_data,
                    poderes=poderes_data,
                    foto=foto_data  # MUDANÇA AQUI: Adiciona a foto
                )

        # 3. REDIRECIONA
        return redirect('perfil') 

    # 4. RENDERIZA A PÁGINA (Lógica GET)
    context = {
        'perfil': perfil,
        'tipo_perfil': tipo,
        'profile_exists': profile_exists
    }
    return render(request, 'editar_perfil.html', context)

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

