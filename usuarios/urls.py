from django.urls import path
from . import views
from feed import views as feed_views
from perfil import views as perfil_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/logout', views.logout_view, name='logout'),
    path('plataforma/', feed_views.plataforma, name='plataforma'), # vou realizar desta forma, a partir desse app, eu importo o app feed.
    path('plataforma/criar_post', feed_views.criar_post, name='criar_post'), # vou realizar desta forma, a partir desse app, eu importo o app feed.
    path('plataforma/perfil', perfil_views.perfil, name='perfil'),
    path('plataforma/perfil/editar_post/<int:id>/', perfil_views.editar_post, name='editar_post'),
]