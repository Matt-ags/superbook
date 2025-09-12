from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Post, Pow, Comentario

@login_required(login_url='/auth/login/')
def comentar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        mensagem = request.POST.get("mensagem")
        if mensagem.strip():  # evitar comentário vazio
            Comentario.objects.create(
                autor=request.user,
                post=post,
                mensagem=mensagem
            )
    return redirect("plataforma")
