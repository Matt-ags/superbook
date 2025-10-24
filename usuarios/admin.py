from django.contrib import admin
from .models import Perfil



from django.contrib import admin

admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"


# Register your models here.
@admin.register(Perfil)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['user', 'descricao', 'poderes']
    list_filter = ['user']
    search_fields = ['user', 'descricao', 'poderes']

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