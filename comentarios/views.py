from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import Comentario

@login_required(login_url='/auth/login/')
def post_detalhes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post).order_by("criado_em")

    if request.method == "POST":
        mensagem = request.POST.get("mensagem")
        if mensagem.strip():  # evitar comentário vazio
            Comentario.objects.create(
                autor=request.user,
                post=post,
                mensagem=mensagem
            )
        return redirect("comentarios:detalhes_post", post_id=post.id)

    return render(request, "post_detalhes.html", {
        "post": post,
        "comentarios": comentarios
    })
