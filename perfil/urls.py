from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil, name='perfil'),
    path('editar_post/<int:id>/', views.editar_post, name='editar_post'),
]
