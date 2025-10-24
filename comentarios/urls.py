from django.urls import path
from . import views

app_name = "comentarios"

urlpatterns = [
    path('<int:post_id>/', views.post_detalhes, name='detalhes_post'),
]
