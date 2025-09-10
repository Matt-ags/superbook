from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil_villain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    poderes = models.TextField(blank='Nenhum')
    email_contato = models.TextField(blank='Nenhum')
