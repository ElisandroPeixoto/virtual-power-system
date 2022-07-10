from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  # Página de Administração
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),  # Página Inicial
    path('', include('usuarios.urls')),  # Páginas do app Usuarios
    path('', include('subestacao.urls'))  # Páginas do app Subestacao
]

admin.site.site_header = 'Virtual Power System'
admin.site.site_title = 'Virtual Power System'
admin.site.index_title = 'Administração do Sistema'
