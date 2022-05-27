from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CriarCustomUsuario, AlterarCustomUsuario
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CriarCustomUsuario
    form = AlterarCustomUsuario
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'pais', 'estado', 'cidade', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'pais', 'estado', 'cidade')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )
