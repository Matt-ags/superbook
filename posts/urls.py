from django.urls import path
from . import views

urlpatterns = [
    path('comentar/<int:post_id>/', views.comentar_post, name='comentar'),
]
