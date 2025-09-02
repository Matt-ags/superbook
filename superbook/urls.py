from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls'))
]
