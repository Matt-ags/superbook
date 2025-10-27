from django.contrib import admin
from django.urls import path, include
# from usuarios import views  <-- NÃO PRECISAMOS MAIS DESTA LINHA
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/auth/login/', permanent=True), name='home'),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # <-- Adicione esta linha

    # apps
    path('auth/', include('usuarios.urls')),
    path('plataforma/', include('feed.urls')),
    path('plataforma/perfil/', include('perfil.urls')),
    path('plataforma/posts/', include('comentarios.urls')),

    # viloes
    path('viloes/', include('viloes.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:

    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]