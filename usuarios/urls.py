from django.urls import path
from .views import login, cadastro, perfil, logout, gerenciar_perfil, alterar_senha, selecao_simulacao

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('inicio/', logout, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/gerenciar_perfil/', gerenciar_perfil, name='gerenciar_perfil'),
    path('perfil/alterar_senha/', alterar_senha, name='alterar_senha'),
    path('selecao_simulacao/', selecao_simulacao, name='selecao_simulacao'),
]
