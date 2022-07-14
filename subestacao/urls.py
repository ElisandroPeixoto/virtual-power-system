from django.urls import path
from .views import subestacao_simulacao

urlpatterns = [
    path('subestacao_simulacao/', subestacao_simulacao, name='subestacao_simulacao'),
]
