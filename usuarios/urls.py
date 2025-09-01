from django.urls import path
from . import views
from feed import views as feed_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', feed_views.plataforma, name='plataforma'), # vou realizar desta forma, a partir desse app, eu importo o app feed.
]