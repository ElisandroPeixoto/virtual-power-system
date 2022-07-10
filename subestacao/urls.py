from django.urls import path
from .views import selecao_simulacao, subestacao_simulacao

urlpatterns = [
    path('selecao_simulacao/', selecao_simulacao, name='selecao_simulacao'),
    path('subestacao_simulacao/', subestacao_simulacao, name='subestacao_simulacao'),
]
