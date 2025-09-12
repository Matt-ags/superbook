from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.autor.codinome}: {self.mensagem[:30]}..."

class Pow(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name="likes", on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('autor', 'post') 

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.id}"
