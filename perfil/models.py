from django.db import models

# Create your models here.
# aqui vai ser o db de usuarios

class Hero(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    # nome_real = models.CharField(max_length=100, blank=True, null=True)
    poderes = models.TextField(blank=True, null=True)
    # cidade = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codinome