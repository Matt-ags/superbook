from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # <-- Adicione esta linha

    # apps
    # path('auth/', include('usuarios.urls')),
    path('plataforma/', include('feed.urls')),
    path('plataforma/perfil/', include('perfil.urls')),
    path('plataforma/posts/', include('comentarios.urls')),

    # viloes
    path('viloes/', include('viloes.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # --- HACK PARA SERVIR MÍDIA TEMPORÁRIA NO RENDER ---
    # Isso é inseguro e ineficiente para produção real,
    # mas funciona para "ver a lógica".
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]