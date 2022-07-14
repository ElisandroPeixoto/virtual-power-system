from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import selecao_simulacao

urlpatterns = [
    path('admin/', admin.site.urls),  # Página de Administração
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),  # Página Inicial
    path('selecao_simulacao/', selecao_simulacao, name='selecao_simulacao'),  # Página Seleção de Simulação
    path('', include('usuarios.urls')),  # Páginas do app Usuarios
    path('', include('subestacao.urls'))  # Páginas do app Subestacao
]

admin.site.site_header = 'Virtual Power System'
admin.site.site_title = 'Virtual Power System'
admin.site.index_title = 'Administração do Sistema'
