from django.urls import path
from .views import login, cadastro, perfil, logout, gerenciar_perfil

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('inicio/', logout, name='logout'),
    path('perfil/gerenciar_perfil/', gerenciar_perfil, name='gerenciar_perfil')
]
