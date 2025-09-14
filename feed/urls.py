from django.urls import path
from . import views

urlpatterns = [
    path('', views.plataforma, name='plataforma'),  
    path('like/<int:post_id>/', views.like, name='like'),
    path('criar_post/', views.criar_post, name='criar_post'),
    path('logout/', views.logout_view, name='logout')

]
