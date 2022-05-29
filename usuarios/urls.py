from django.urls import path
from .views import login, cadastro, perfil, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('inicio/', logout, name='logout')
]
