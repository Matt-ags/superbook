from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    cc_myself = models.CharField(max_length=100)  # aqui pode ser "poderes" ou algo que queira
