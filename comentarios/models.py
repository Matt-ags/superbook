from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.id}"
