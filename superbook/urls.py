from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listar, name='listar'),
    path('admin/', admin.site.urls),

    # apps
    path('auth/', include('usuarios.urls')),
    path('plataforma/', include('feed.urls')),
    path('plataforma/perfil/', include('perfil.urls')),
    path('plataforma/posts/', include('comentarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
