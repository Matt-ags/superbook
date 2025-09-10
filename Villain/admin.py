from django.contrib import admin
from .models import Perfil_villain

# Register your models here.
@admin.register(Perfil_villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['user', 'descricao', 'poderes', 'email_contato']
    list_filter = ['user']
    search_fields = ['user', 'descricao', 'poderes', 'email_contato']

    # fieldsets = (
    #     ('Usuário', {
    #         'fields': ('user')
    #     }),
    #     ('História', {
    #         'fields': ('descricao')
    #     }),
    #     ('Poderes', {
    #         'fields': ('descricao')
    #     }),
    # )
    # readonly_fields = ['user']