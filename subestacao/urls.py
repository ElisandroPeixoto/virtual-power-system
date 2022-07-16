from django.urls import path
from .views import subestacao_simulacao, al1

urlpatterns = [
    path('subestacao_simulacao/', subestacao_simulacao, name='subestacao_simulacao'),
    path('subestacao_simulacao/AL1', al1, name='al1'),
]
