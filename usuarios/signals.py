from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Importa os sinais do allauth (para login social/google)
from allauth.account.signals import user_signed_up

# Importe seus modelos de perfil
# (Se Perfil_viloes também estivesse aqui, importaria)
from .models import Perfil 

@receiver(user_signed_up)
def create_profile_on_social_signup(request, user, **kwargs):
    """
    Cria um perfil padrão quando um usuário se cadastra 
    via Google ou outra rede social.
    """
    # Cria um Perfil de 'herói' como padrão.
    # Você pode mudar a descrição padrão se quiser.
    if not Perfil.objects.filter(user=user).exists():
        Perfil.objects.create(
            user=user, 
            descricao="Novo aventureiro pronto para a jornada!"
        )

@receiver(post_save, sender=User)
def create_profile_on_local_signup(sender, instance, created, **kwargs):
    """
    Cria um perfil padrão quando um usuário se cadastra 
    localmente (com usuário e senha).
    """
    if created: # 'created' é True apenas na primeira vez que o User é salvo
        # Verifica se um perfil social já não foi criado (evita duplicar)
        if not Perfil.objects.filter(user=instance).exists():
            Perfil.objects.create(
                user=instance, 
                descricao="Novo aventureiro pronto para a jornada!"
            )